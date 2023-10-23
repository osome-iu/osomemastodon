"""
Purpose:
    This script is used to get the timeline statuses of the API.
    Doc -
Inputs:
    -
Output:
    JSON file of statuses
Authors: Pasan Kamburugamuwa
"""

import requests
import pandas as pd
import os, json
from library import backend_util

# Log file location and the file
LOG_DIR = "/home/data/apps/mastodon/log"
LOG_FNAME = "mastodon_logging.log"

script_name = os.path.basename(__file__)
logger = backend_util.get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)

def fetch_timeline_status_data(mastodon_instance, limit, data_type):
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
    timeline_statuses_endpoint_url = f'https://{mastodon_instance}/api/v1/timelines/public?limit={limit}&local={data_type}'
    response = requests.get(timeline_statuses_endpoint_url)
    # Check the response status code
    if response.status_code == 200:
        timeline_data = response.json()
        print(timeline_data)
        timeline_statuses = {"timeline_statuses": timeline_data}
        return timeline_statuses
    else:
        # Handle the errors occur with API method calling.
        logger.error(f"Error: {response.status_code} - {response.text}")
