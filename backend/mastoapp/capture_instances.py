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

# Log file location and the file
LOG_DIR = "/home/data/apps/mastodon/log"
LOG_FNAME = "mastodon_logging.log"

FILE = "/home/data/apps/mastodon/osomemastodon/backend/data/mastodon_instance.json"

script_name = os.path.basename(__file__)
logger = backend_util.get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)
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
    url = "https://instances.social/api/1.0/instances/list?min_active_users=5000&count=20&sort_by=statuses&sort_order=asc"
    payload={}
    headers = {
        'Authorization': 'Bearer ' + backend_util.get_instances_social_api_key()
    }
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        instance_list = []
        for instance in data.get("instances", []):

            instance_name = instance.get("name")
            active_users = instance.get("active_users")
            all_users = instance.get("users")

            #This function is used to write the collected instance_name in to a json file.
            if instance_name:
                # Create a dictionary with only the "name" field
                instance_list.append({"name": instance_name, "active_users": active_users, "all_users": all_users})

                with open(FILE, 'w') as json_file:
                    json.dump(instance_list, json_file, indent=2)
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


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
    with open(FILE, 'r') as file:
        data = json.load(file)

    json_data = json.dumps(data, indent=2)
    return json_data


