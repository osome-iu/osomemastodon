"""
Purpose:
    This script is used to store the mastodon instance details along with each instance's characteristics
Inputs:
    Bearer token of the instances social API key
Output:
    Save the details on a txt file.
Authors: Pasan Kamburugamuwa
"""

import requests
import pandas as pd
import os, json
from library import backend_util

def save_instance_data(data):
    """
    Save the data on txt file and csv file.

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
    filename = 'data/mastodon_instance_info.csv'
    cols = ['Name', 'URL', 'Description', 'Logo', 'Users', 'Active Users']
    df = pd.DataFrame(data, columns=cols)
    df.to_csv(filename, index=False)

    ## Save list of instance domains to txt file
    with open('data/mastodon_instance_info.txt', 'w') as f:
        for instance in df['Name']:
            f.write(f"{instance}\n")

def fetch_instance_data():
    """
    Get the instance information from the instances.social API

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
    url = "https://instances.social/api/1.0/instances/list?min_active_users=5000&count=20&sort_by=statuses&sort_order=desc"
    payload={}
    headers = {
        'Authorization': 'Bearer ' + backend_util.get_instances_social_api_key()
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    return data

