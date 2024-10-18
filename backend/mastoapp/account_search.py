"""
Purpose:
    This script is used to search the account information of each mastodon instances
Inputs:
    Account Id and mastodon instance name.
Output:
    Save the details on a txt file.
Authors: Pasan Kamburugamuwa
"""

import requests
import pandas as pd
import os, json
from library import backend_util

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

