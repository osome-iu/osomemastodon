################################### This file saves a list of mastodon instances along with their characteristics ###################################

import requests
import pandas as pd
import os, json

class CaptureMastoInstances:
    def __init__(self):
        BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
        credentials = json.load(open(os.path.join(BASE_DIR, "keys.json")))
        self.api_key = credentials['InstancesSocialAPIKey']

    def save_instance_data(self, data):
        ## Save Instance Info to CSV
        filename = '../data/mastodon_instance_info.csv'
        cols = ['Name', 'URL', 'Description', 'Logo', 'Users', 'Active Users']
        df = pd.DataFrame(data, columns=cols)
        df.to_csv(filename, index=False)

        ## Save list of instance domains to txt file
        with open('../data/mastodon_instance_info.txt', 'w') as f:
          for instance in df['Name']:
              f.write(f"{instance}\n")

    def fetch_instance_data(self):
        ## Get Instance information from instances.social api
        # https://instances.social/api/doc/#api-Instances-ListInstances
        url = "https://instances.social/api/1.0/instances/list?min_users=1000&count=10000&sort_by=users&sort_order=desc"
        payload={}
        headers = {
          'Authorization': 'Bearer ' + self.api_key
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

if __name__ == "__main__":
    masto = CaptureMastoInstances()
    masto.fetch_instance_data()