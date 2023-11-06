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

# Log file location and the file
LOG_DIR = "/Users/pkamburu/IUNI/mastodon/backup/untitledfolder2/log"
LOG_FNAME = "mastodon_logging.log"

script_name = os.path.basename(__file__)
logger = backend_util.get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)

def fetch_account_data(mastodon_instance, account_id):
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
    print(account_search_endpoint_url)
    response = requests.get(account_search_endpoint_url)
    print(response)
    # Check the response status code
    if response.status_code == 200:
        account = response.json()
        return account
    else:
        # Handle the errors occur with API method calling.
        logger.error(f"Error: {response.status_code} - {response.text}")
