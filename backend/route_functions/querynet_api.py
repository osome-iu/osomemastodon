"""
Purpose:
    This script used to call the Mastodon data to feed into QueryNet tool.
Inputs:
    - Please update at the end.
Outputs:
    - Please update at the end.
Authors: Pasan Kamburugamuwa
"""
from flask import Blueprint,request,jsonify
from mastoapp import querynet_search
from library import backend_util, network
import os,json

# Define logger
logger = backend_util.get_logger(script_name=os.path.basename(__file__), also_print=True)

# Define blueprint
blueprint = Blueprint('querynet_api', __name__, url_prefix='/api')

test_data_path = '/Users/pkamburu/Mastodon/MastodonInterface/osomemastodon/backend/test/test_data.json'

@blueprint.route('/get-public-timeline-hashtag-data', methods=['POST'])
def get_public_timeline_posts_by_hashtag():
    """
    Hashtags -
    Search the hashtag data through hashtag keyword.
    """
    try:
        all_collected_data_list = []
        data = request.get_json()

        mastodon_instances = data.get('mstdn_instances')  # Get all the Mastodon instances
        searched_hashtag = data.get('hashtag')  # Get the hashtag information
        limit = data.get('limit') or 40  # Default limit if not provided
        max_results = data.get('max_limit')  # Use 100 if not provided max results

        for mastodon_instance in mastodon_instances:
            name = mastodon_instance.get('name')
            if name:
                since_id = None
                total_results = 0
                instance_results = []

                while total_results < max_results:
                    # Fetch the hashtag data with pagination
                    hashtag_data = querynet_search.public_timeline_search_by_hashtag(
                        name, searched_hashtag, limit, since_id
                    )

                    if not hashtag_data:
                        break  # Stop if no more data is returned

                    # Log received statuses
                    logger.info(f"Received {len(hashtag_data)} statuses from {name}.")

                    # Add instance name to the records
                    for record in hashtag_data:
                        record['instance_name'] = name

                    instance_results.extend(hashtag_data)
                    total_results += len(hashtag_data)

                    # Set `since_id` for pagination (ID of the last status)
                    since_id = hashtag_data[-1]['id']

                    # Stop if max results are reached
                    if total_results >= max_results:
                        break

                logger.info(f"Total number of results received from {name} for the hashtag: {searched_hashtag} is: {total_results}")

                # Trim the results to get the exact number of results.
                instance_results = instance_results[:max_results]

                all_collected_data_list.append(instance_results)

        with open(test_data_path, 'r') as f:
            data = json.load(f)
        json_object = network.process_hashtags(data, 'hoosiersocial')

        # json_object = network.process_hashtags(all_collected_data_list, searched_hashtag)
        print(f"Nodes {len(json_object['nodes'])}")
        print(f"Edges {len(json_object['edges'])}")
        return jsonify(json_object)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return "Bad request", 400

@blueprint.route('/get-friends-info', methods=['POST'])
def get_account_friends():
    """
    Search for accounts based on a search keyword and return the results.
    """
    try:
        data = request.get_json()

        mastodon_instance = data.get("instance") # Get the instance
        searched_keyword = data.get('searched_keyword')  # Get the account search keyword.
        limit = data.get('limit') or 40  # Default to 40 if not provided access token
        max_limit = data.get('max_limit') or 200  # Default to 200 if not provided for max results
        friend_info_type = data.get('type') # Friends info type

        # Ensure limit is capped at max_limit
        if limit > max_limit:
            limit = max_limit

        # Fetch the accounts using the search function
        all_collected_accounts = querynet_search.get_accounts_by_search_keyword(mastodon_instance, searched_keyword, limit, friend_info_type)

        # Return the fetched accounts as a JSON response
        return jsonify(all_collected_accounts)

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return "Bad request", 400

