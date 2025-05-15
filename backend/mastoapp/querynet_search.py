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
from urllib.parse import urlparse
from library import backend_util
from flask import jsonify

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
            'limit': limit,
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

def account_lookup_api(domain, username):
    """
    Quickly lookup a username to see if it is available, skipping WebFinger resolution.

    Reference - https://docs.joinmastodon.org/methods/accounts/#lookup
    Parameters
    -----------
    - domain: The Mastodon domain in query
    - username: Unique username in the particular Mastodon instance.

    Returns
    - List of JSON objects representing statuses.
    """

    # Header for the request
    headers = {
        'User-Agent': 'curl/7.68.0',  # Mimic curl's User-Agent
    }

    account_lookup_endpoint = f'https://{domain}/api/v1/accounts/lookup'
    params = {"acct": username}

    try:
        response = requests.get(account_lookup_endpoint, params = params, headers = headers)
        return response.json() # Return the data
    except requests.exceptions.RequestException as e:
        logger.error(f"HTTP error occurred while processing account lookup in {domain} with username {username}: {e}")
    except Exception as e:
        logger.error(f"Error in processing account in {domain} with username : {username}")


def get_friends_info(mastodon_instance, account_id, friends_info_type, limit):
    """
    Friends info calling API, this is a common function to grab both Mastodon followings and followers
    for the given account id.

    Reference - https://docs.joinmastodon.org/methods/accounts/#followers
    Parameters
    -----------
    - mastodon_instance: The Mastodon instance to query.
    - id: Unique post id.

    Returns
    - List of JSON objects representing statuses.
    """
    all_friends_info = []

    # Header for the request
    headers = {
        'User-Agent': 'curl/7.68.0',  # Mimic curl's User-Agent
    }

    # Base URL with required parameters
    get_friends_info_endpoint = f'https://{mastodon_instance}/api/v1/accounts/{account_id}/{friends_info_type}'
    params = {'limit': limit}

    while True:
        response = requests.get(get_friends_info_endpoint, params=params, headers=headers)

        if response.status_code != 200:
            logger.error(f"Failed to retrieve friends information for the instance {mastodon_instance} with account id : {account_id}")
            break

        try:
            # receive the friends information
            friends_info = response.json()

        except JSONDecodeError:
            logging.error(f"JSON decode error: {response.text}")
            break

        if not friends_info:
            break

        all_friends_info.extend(friends_info)

        links = response.headers.get('Link', '')
        next_link = None
        for link in links.split(','):
            if 'rel="next"' in link:
                next_link = link.split(';')[0].strip('<>')
                break
        if next_link:
            params = {param.split('=')[0]: param.split('=')[1] for param in next_link.split('?')[1].split('&')}
        else:
            break

    return all_friends_info

def check_valid_mastodon_instance(mstd_instance):
    """
    Check if the given Mastodon instance is valid by sending a GET request
    to the /api/v1/instance endpoint.

    inputs:
        mstd_instance (str): The Mastodon instance URL (without 'https://').

    returns:
        bool: True if the instance is valid, False otherwise.
    """
    api_url = f"https://{mstd_instance}/api/v1/instance"
    try:
        response = requests.get(api_url, headers={'Content-Type': 'application/json'})
        return response.ok
    except requests.RequestException as error:
        print('Error during API request:', error)
        return False

def get_domain_and_post_id(user_identifier):
    """
    Extract the domain and post id.

    inputs:
        url (str): The Mastodon instance URL (without 'https://').

    returns:
        bool: True if the instance is valid, False otherwise.
    """
    # Parse the user identifier
    parsed_url = urlparse(user_identifier)
    domain = parsed_url.netloc

    path_parts = parsed_url.path.split('/')
    post_id = path_parts[-1]

    return domain, post_id


def fetch_api_data(url, headers, post_id, instance_name, data_key):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"HTTP {response.status_code} error for {url}")
    except requests.RequestException as error:
        logger.error(f"Error - {error} occurred while retrieving data from domain: {instance_name} and post Id: {post_id}")
    return None


def querynet_keyword_search(access_token: str, search_keyword: str, mastodon_instance: str,
                            limit: int = 20, max_limit: int = None) -> dict:
    """
    Searches for statuses on a Mastodon instance using a keyword.

    Parameters:
    - access_token: Bearer token to authenticate (None for public access)
    - search_keyword: Term to search for
    - mastodon_instance: Instance domain (e.g., "mastodon.social")
    - limit: Per-request limit (default 20, max 40 when authenticated)
    - max_limit: Total maximum results to return (optional)

    Returns dict with 'statuses' array and metadata
    """
    base_url = f'https://{mastodon_instance}/api/v2/search'
    headers = {'Authorization': f'Bearer {access_token}'} if access_token else {}
    all_statuses = []

    params = {
        'q': search_keyword,
        'type': 'statuses',
        'limit': min(int(limit), 40) if access_token else min(int(limit), 5),
    }

    if access_token:
        params.update({
            'resolve': 'true',
            'offset': 0,
        })

    try:
        while True:
            response = requests.get(base_url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            statuses = data.get('statuses', [])
            if not statuses:
                break

            all_statuses.extend(statuses)

            # Check max limit
            if max_limit and len(all_statuses) >= max_limit:
                all_statuses = all_statuses[:max_limit]
                break

            # Pagination handling
            if access_token:
                if len(statuses) < params['limit']:
                    break
                params['offset'] += params['limit']
            else:
                break

    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP error in search: {err}")
        return {'error': str(err), 'status_code': getattr(err.response, 'status_code', None)}
    except Exception as e:
        logger.error(f"Search error: {e}")
        return {'error': str(e)}

    return {
        'statuses': all_statuses,
        'metadata': {
            'count': len(all_statuses),
            'instance': mastodon_instance,
            'authenticated': bool(access_token)
        }
    }

def retrieve_posts_replies_and_boosts(posts):
    """
    Get the reblogged accounts and replies for each post - https://docs.joinmastodon.org/methods/statuses/#boost
    Getting the parent and child context for posts - https://docs.joinmastodon.org/methods/statuses/#context
    """
    all_posts = []
    headers = {'User-Agent': 'curl/7.68.0'}

    for post in posts:
        domain, post_id = get_domain_and_post_id(post.get('uri'))

        if post.get('reblogs_count', 0) > 0:

            reblogged_url = f"https://{domain}/api/v1/statuses/{post_id}/reblogged_by"
            post['reblogged_users'] = fetch_api_data(reblogged_url, headers, post_id, domain, 'reblogged_users')

        replies_url = f"https://{domain}/api/v1/statuses/{post_id}/context"
        post['replies'] = fetch_api_data(replies_url, headers, post_id, domain, 'replies')

        all_posts.append(post)
    return all_posts










