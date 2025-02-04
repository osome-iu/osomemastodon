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
        is_diffusion_network = data.get("is_diffusion_network") or False # Get the diffusion network

        logger.info(f"Start collecting data for Mastodon co-occurrence network with hashtag: {searched_hashtag} on {mastodon_instances} with limit {limit}")

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

        if is_diffusion_network:
            # To grab the reblogged accounts
            all_collected_data_list = querynet_search.get_rebloged_accounts(all_collected_data_list)

        # json_object = network.process_hashtags(all_collected_data_list, searched_hashtag)
        logger.info(f"End of retrieving Mastodon co-occurrence network with given hashtag")
        return jsonify(all_collected_data_list)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return "Bad request", 400


@blueprint.route('/get-accounts-search-by-keyword', methods=['POST'])
def get_accounts_by_searched_keyword():
    """
    Get accounts by searched keyword.
    """
    try:
       data = request.get_json()
       mastodon_instances = data.get('mstdn_instances')
       searched_keyword = data.get('keyword')
       limit = data.get('limit') # This is for the future use.

       logger.info(f"Start collecting accounts for the given keyword : {searched_keyword} on {mastodon_instances}")
       unique_accounts = {}

       for mstdn_instance in mastodon_instances:
           instance_results = querynet_search.get_accounts_by_search_keyword(mstdn_instance.get("name"), searched_keyword, limit)

           for account in instance_results:
               acct = account.get("acct")
               if acct and acct not in unique_accounts:
                   unique_accounts[acct] = account
       # Unique accounts
       all_collected_accounts = list(unique_accounts.values())

    except Exception as e:
        logger.error(f"Error in retrieving accounts for the given hashtag {e}")
        return "Bad request", 400
    else:
        logger.info(f"Retrieved {len(all_collected_accounts)} for the searched hashtag {searched_keyword}")
        return jsonify(all_collected_accounts)



