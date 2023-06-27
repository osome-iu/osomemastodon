"""
Purpose:
    This script is used to store the mastodon instance details along with each instance's characteristics
Inputs:
    Bearer token of the instances social API key
Output:
    Save the details on a txt file.
Authors: Rishab Ravi and Pasan Kamburugamuwa
"""
import requests
import pandas as pd
import os, json
from library import backend_util

class CaptureMastodonInstances:
    def save_instance_data(self, data):
        """
        Save the data on txt file and csv file.

        Parameters
        -----------
        - Pass the instance social media key (get from here - https://instances.social/api/token)

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

    def fetch_instance_data(self):
        """
        Get the instance information from the instances.social API

        Parameters
        -----------
        - Pass the instance social media key (get from here - https://instances.social/api/token)

        Returns
        - name - name of the instance
        - short_description - short description of the instance
        - thumbnail - thumbnail
        - users - no of users
        - active_users - no of activate users
        -----------
        """
        url = "https://instances.social/api/1.0/instances/list?min_users=1000&count=10000&sort_by=users&sort_order=desc"
        payload={}
        headers = {
          'Authorization': 'Bearer ' + backend_util.get_instances_social_api_key()
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        instance_data = []
        for instance in data['instances']:
            instance_name = instance['name']
            instance_url = 'https://' + instance['name']
            instance_description = instance['info']['short_description']
            instance_logo = instance['thumbnail']
            num_users = instance['users']
            num_active_users = instance['active_users']
            instance_data.append([instance_name, instance_url, instance_description, instance_logo, num_users, num_active_users])
        self.save_instance_data(instance_data)
