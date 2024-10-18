"""
Purpose:
    This script is used to call the API endpoints and collect data.
Inputs:
    - Please update at the end.
Outputs:
    - Please update at the end.
Authors: Pasan Kamburugamuwa
"""
import os
import requests
from library import backend_util

# Define the logger
logger = backend_util.get_logger(script_name=os.path.basename(__file__), also_print=True)

def public_timeline_search_by_hashtag(mastodon_instance, hashtag, limit, since_id=None):
    """
    This API call is used to get public timeline posts by hashtag with optional pagination support.

    Reference - https://docs.joinmastodon.org/methods/timelines/#tag
    Parameters
    -----------
    - mastodon_instance: The Mastodon instance to query.
    - hashtag: The hashtag to search for.
    - limit: The number of results to retrieve (up to 40).
    - since_id: (Optional) The ID to use for pagination, to get results newer than this ID.

    Returns
    - List of JSON objects representing statuses.
    """
    try:
        # Header (this applies to some of the Mastodon instances, as it will need to have VPN to connect)
        header = {
            'User-Agent': 'curl/7.68.0',  # Mimic curl's User-Agent
        }
        # Base URL with required parameters
        public_hashtag_endpoint = f'https://{mastodon_instance}/api/v1/timelines/tag/{hashtag}?limit={limit}'

        # Append since_id if provided (for pagination)
        if since_id:
            public_hashtag_endpoint += f'&since_id={since_id}'

        response = requests.get(public_hashtag_endpoint, headers=header)

        if response.status_code == 200:
            statuses = response.json()
            logger.info(f"Get public timeline posts of {mastodon_instance} by the hashtag: {hashtag}, statuses received: {len(statuses)}")
            return statuses
        else:
            logger.error(f"Failed to get hashtag data from {mastodon_instance}. Status code: {response.status_code}")
            return []
    except Exception as e:
        logger.error(f"Error occurred retrieving the data - {e}")


def get_accounts_by_search_keyword(mastodon_instance, search_keyword, limit):
    """
    Get the list of user accounts based on search keyword.

    Reference - https://docs.joinmastodon.org/methods/search/
    Parameters
    -----------
    - mastodon_instance: The Mastodon instance to query.
    - search_keyword: Keyword searched.
    - limit: The number of results to retrieve (up to 200 or more with pagination).

    Returns
    - List of JSON objects representing user accounts.
    """

    # Header for the request
    headers = {
        'User-Agent': 'curl/7.68.0',  # Mimic curl's User-Agent
    }

    # Base URL for the search endpoint
    search_url = f'https://{mastodon_instance}/api/v2/search'

    # Accumulate the accounts
    accounts = []
    offset = 0
    fetch_limit = 40

    while len(accounts) < limit:
        # Determine how many results to request in this iteration
        current_limit = min(fetch_limit, limit - len(accounts))

        # Prepare request parameters
        params = {
            'q': search_keyword,
            'type': 'accounts',
            'limit': 40,
            'resolve': 'false'
        }

        # Make the request to the Mastodon instance
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()  # Ensure the request was successful

        # Parse the JSON response
        data = response.json()

        # Append the retrieved accounts to the list
        accounts.extend(data.get('accounts', []))

        offset += current_limit

        # Stop if no more accounts are returned
        if len(data.get('accounts', [])) == 0:
            break

    # Return the accumulated accounts
    return accounts


def get_friends_info(mastodon_instance, account_id, friends_info_type='followers'):
    """
    Friends info calling API

    Reference - https://docs.joinmastodon.org/methods/accounts/#followers
    Parameters
    -----------
    - mastodon_instance: The Mastodon instance to query.
    - id: Unique post id.

    Returns
    - List of JSON objects representing statuses.
    """

    # Header for the request
    headers = {
        'User-Agent': 'curl/7.68.0',  # Mimic curl's User-Agent
    }

    # Base URL with required parameters
    get_friends_info = f'https://{mastodon_instance}/api/v1/accounts/{account_id}/{friends_info_type}'
    return "Test"




