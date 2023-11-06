"""
Purpose:
    This script is used to search the hashtag in a public timeline.
    Doc -
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

def fetch_hashtag_data(mastodon_instance, hashtag, data_type, limit):
    """
    Get the public hashtag information from the mastodon API.
    Documentation - https://docs.joinmastodon.org/methods/timelines/#public
    Parameters
    -----------
    - Pass the account id, mastodon instance name

    Returns
    - Json object which contains the account information.
    -----------
    """
    hashtag_search_endpoint_url = f'https://{mastodon_instance}/api/v1/timelines/tag/{hashtag}?limit={limit}&local={data_type}'

    response = requests.get(hashtag_search_endpoint_url)
    hashtag_data = {}
    # Check the response status code
    if response.status_code == 200:
        hashtag_data = response.json()
        hashtag_dict = {"hashtag": hashtag_data}
        return hashtag_dict
    else:
        # Handle the errors occur with API method calling.
        logger.error(f"Error: {response.status_code} - {response.text}")