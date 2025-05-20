import os
import requests
import json
from library import backend_util

#########################################################
############## Mastodon instances ##################
#########################################################

# Define the logger
logger = backend_util.get_logger(script_name=os.path.basename(__file__), also_print=True)

def get_all_instance_from_saved_file():
    """
    This will grab all the instances from the saved json file.

    Parameters
    -----------
    - Pass the instance social media key (get from here - https://instances.social/api/doc/)

    Returns
    - name - name of the instance
    - short_description - short description of the instance
    - thumbnail - thumbnail
    - users - no of users
    - active_users - no of activate users
    -----------
    """
    with open(backend_util.get_instances_file(), 'r') as file:
        data = json.load(file)

    # Exact the name only
    names_list = [{"name": item['name']} for item in data['instances']]

    # Convert the list of names to a JSON array with indentation
    json_data = json.dumps(names_list, indent=2)
    return json_data

#########################################################
############## Mastodon account search ##################
#########################################################
def fetch_account_data_by_account_id(mastodon_instance, account_id):
    """
    Get the account information from the mastodon API.
    Documentation - https://docs.joinmastodon.org/methods/accounts/#get
    Parameters
    -----------
    - Pass the account id, mastodon instance name

    Returns
    - Json object which contains the account information.
    -----------
    """
    account_search_endpoint_url = f'https://{mastodon_instance}/api/v1/accounts/{account_id}'
    response = requests.get(account_search_endpoint_url)
    # Check the response status code
    if response.status_code == 200:
        account = response.json()
        return account
    else:
        # Handle the errors occur with API method calling.
        logger.error(f"Error: {response.status_code} - {response.text}")
        return response.status_code

def get_account_data_from_keyword(mastodon_instance, search_keyword):
    """
    Get the account data from the keyword.
    Parameters
    -----------
    - Pass the mastodon_instance, keyword

    Returns
    - Json object which contains the account information.
    -----------
    Note: here is the reference : https://docs.joinmastodon.org/methods/search/
    """
    try:
        search_endpoint_url = f'https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=accounts'

        response = requests.get(search_endpoint_url)

        # Check the response status code
        if response.status_code == 200:
            results_array = response.json()
            account_data = {"results": results_array}
        else:
            account_data = {"error_search_not_allowed": "Bad request (400 error)"}

    except (requests.exceptions.HTTPError, Exception) as err:
        # Handle HTTP errors (4xx or 5xx) here
        account_data = {"error_search_not_allowed": "Bad request (400 error)"}

    return account_data


#########################################################
########## Mastodon statuses timeline search ############
#########################################################

def fetch_timeline_status_data(mastodon_instance, data_type, limit):
    """
    Get the public timeline data from the mastodon instances
    Documentation - https://docs.joinmastodon.org/methods/timelines/#public
    Parameters
    -----------
    - Nothing

    Returns
    - Json object which contains the statuses
    -----------
    """
    try:
        timeline_statuses_endpoint_url = f'https://{mastodon_instance}/api/v1/timelines/public?limit={limit}&local={data_type}'
        response = requests.get(timeline_statuses_endpoint_url)

        # Check the response status code
        if response.status_code == 200:
            timeline_data = response.json()
            timeline_status = {"statuses_timeline": timeline_data}
        else:
            timeline_status = {"error_search_not_allowed": "Bad request (400 error)"}

    except (requests.exceptions.HTTPError, Exception) as err:
        # Handle HTTP errors (4xx or 5xx) here
        timeline_status = {"error_search_not_allowed": "Bad request (400 error)"}
    return timeline_status

#########################################################
############## Mastodon statuses search #################
#########################################################
def status_search_by_id(mastodon_instance, status_id):
    """
    This method is used to search the statuses from status's id

    Parameters passing
    -----------
    - status_id - status_id
    - mastodon_instance - name of the mastodon instance
    Returns
    - JSON object
        {
            "id": "1",
            "created_at": "2016-03-16T14:44:31.580Z",
            "in_reply_to_id": null,
            "in_reply_to_account_id": null,
            "sensitive": false,
            "spoiler_text": "",
            "visibility": "public",
            "language": "en",
            "uri": "https://mastodon.social/users/Gargron/statuses/1",
            "url": "https://mastodon.social/@Gargron/1",
            "replies_count": 7
            ...
        }
        -----------
    """
    status_endpoint_url = f'https://{mastodon_instance}/api/v1/statuses/{status_id}'
    response = requests.get(status_endpoint_url)
    status = response.json()
    return status


def mastodon_search_by_keyword(access_token, search_keyword, mastodon_instance):
    """
    This method is used to get the accounts, statuses, and hashtags.

    Parameters:
    - access_tokens - Bearer tokens to retrieve statuses
    - search_keyword - search keyword

    Returns:
    - JSON object
        "accounts": [...],
        "statuses": [...],
        "hashtags": [...]

    Note: Reference - https://docs.joinmastodon.org/methods/search/
    """
    search_endpoint_url = f'https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=statuses&resolve=true'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    try:
        response = requests.get(search_endpoint_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        if response.status_code == 200:
            results_array = response.json()
            searched_status = {"results": results_array}

    except requests.exceptions.HTTPError as err:
        # Handle HTTP errors (4xx or 5xx) here
        searched_status = {"error_search_not_allowed": "Bad request (400 error)"}

    except Exception as e:
        # Handle other exceptions here
        searched_status = {"error_search_access_key": f"An unexpected error occurred: {e}"}

    return searched_status


#########################################################
############## Mastodon hashtag search ##################
#########################################################
def fetch_hashtag_data(mastodon_instance, hashtag, data_type, limit):
    """
    This is for the timeline hashtag data.
    Get the public hashtag information from the mastodon API.
    Documentation - https://docs.joinmastodon.org/methods/timelines/#public
    Parameters
    -----------
    - Pass the account id, mastodon instance name

    Returns
    - Json object which contains the account information.
    -----------
    """
    try:
        hashtag_search_endpoint_url = f'https://{mastodon_instance}/api/v1/timelines/tag/{hashtag}?limit={limit}&local={data_type}'

        response = requests.get(hashtag_search_endpoint_url)

        # Check the response status code
        if response.status_code == 200:
            results_array = response.json()
            hashtag_data = {"statuses_timeline": results_array}
        else:
            hashtag_data = {"error_search_not_allowed": "Bad request (400 error)"}

    except (requests.exceptions.HTTPError, Exception) as err:
        # Handle HTTP errors (4xx or 5xx) here
        hashtag_data = {"error_search_not_allowed": "Bad request (400 error)"}

    return hashtag_data


def get_hashtag_data_from_keyword(mastodon_instance, search_keyword):
    """
    Hashtag metadata
    Get the hashtag data from the keyword.
    Parameters
    -----------
    - Pass the mastodon_instance, keyword

    Returns
    - Json object which contains the hashtag information.
    -----------
    Note: here is the reference : https://docs.joinmastodon.org/methods/search/
    """
    try:
        search_endpoint_url = f'https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=hashtags'

        response = requests.get(search_endpoint_url)

        # Check the response status code
        if response.status_code == 200:
            results_array = response.json()
            hashtag_data = {"results": results_array}
        else:
            hashtag_data = {"error_search_not_allowed": "Bad request (400 error)"}

    except (requests.exceptions.HTTPError, Exception) as err:
        # Handle HTTP errors (4xx or 5xx) here
        hashtag_data = {"error_search_not_allowed": "Bad request (400 error)"}

    return hashtag_data