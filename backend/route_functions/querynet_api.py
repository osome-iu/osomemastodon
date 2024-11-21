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

        json_object = network.process_hashtags(all_collected_data_list, searched_hashtag)
        return jsonify(json_object)
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


@blueprint.route('/get-friends-follower-network', methods=['POST'])
def build_follower_network():
    """
    Search for accounts based on a search keyword and return the results.
    """
    try:
        data = request.get_json()

        account_url = data.get("acct_url")  # Get the account URL
        limit = data.get('limit') or 40     # Default to 40 if not provided
        friend_info_type = data.get('type') or 'following'  # Default to 'following'

        # Get domain and username from account URL
        acct_domain, acct_username = querynet_search.get_domain_and_username(account_url)

        # Check if the Mastodon instance is valid
        if not querynet_search.check_valid_mastodon_instance(acct_domain):
            logger.error(f"Invalid Mastodon instance : {acct_domain}")
            return "Invalid Mastodon instance", 400

        # Retrieve account ID based on the domain and username
        account_info = querynet_search.account_lookup_api(acct_domain, acct_username)
        if not account_info:
            logger.error(f"Account not found with the domain : {acct_domain}")
            return "Account not found", 404

        # Retrieve friend or follower information
        acct_friends_info = querynet_search.get_friends_info(acct_domain, account_info["id"], friend_info_type, limit)

        # Initialize the network structure
        follower_network = {
            "nodes": [],  # Each node represents a user account
            "edges": []   # Each edge represents a follow relationship
        }

        # Add the main account as the center node
        main_node = {
            "acct_url": account_info["url"],
            "acct": account_info["acct"],
            "display_name": account_info.get("display_name", account_info["acct"]),
            "domain": acct_domain,
            "type": "main"
        }

        follower_network["nodes"].append(main_node)

        # Process friends/followers to create nodes and edges
        for friend in acct_friends_info:
            # Skip adding nodes or edges that would create a hair loop
            if friend["url"] == account_info["url"]:
                continue

            # Add each friend/follower as a node
            friend_node = {
                "acct_url": friend["url"],
                "acct": friend["acct"],
                "display_name": friend.get("display_name", friend["acct"]),
                "domain": acct_domain,
                "type": friend_info_type  # Mark as 'following' or 'follower'
            }
            follower_network["nodes"].append(friend_node)

            # Create an edge from the main account to each friend/follower
            edge = {
                "source": main_node["acct_url"],   # Main account URL
                "target": friend["url"]            # Friend/Follower account URL
            }
            follower_network["edges"].append(edge)

        logger.info(f"Successfully retrieved friends follower network for the url {account_url}")
        # Return the network structure as JSON
        return jsonify(follower_network)

    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return "Bad request", 400


