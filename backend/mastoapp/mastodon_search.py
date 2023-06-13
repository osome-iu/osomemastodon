import requests
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
# import time
import httplib2
import urllib.parse
import os, sys

class MastodonSearch:
    def __init__(self):
        self.session = requests.Session()
        retry = Retry(connect=2, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.session.timeout = 5

    def make_endpoint_request(self, endpoint_url, headers=None):
        # print('making request to: ' + endpoint_url)

        try:
            # start_time = time.time()
            response = self.session.get(endpoint_url, headers=headers, timeout=5)
            
            response.raise_for_status()
            # elapsed_time = time.time() - start_time
            #print(f"Request took {elapsed_time:.2f} seconds")
        
        except requests.exceptions.ConnectionError as e:
            #print(f"Error connecting to {endpoint_url}: {e}")
            return None
        except requests.exceptions.HTTPError as e:
            #print(f"Error retrieving data from {endpoint_url}: {e}")
            return None
        except requests.exceptions.RequestException as e:
            #print('endpoint: ' + endpoint_url + ' request failed')
            return None
        except requests.exceptions.Timeout as e:
            # elapsed_time = time.time() - start_time
            #print(f"Request took {elapsed_time:.2f} seconds")
            #print('endpoint: ' + endpoint_url + ' request timed out')
            return None
        
        if response.status_code == 200:
            try:
                result = response.json()
                return result
            except json.decoder.JSONDecodeError as e:
                #print('endpoint: ' + endpoint_url + ' failed to decode JSON')
                return None
        else:
            #print(f"Error {response.status_code}: {response.reason}")
            return None
    
    ## User Search ##
    def request_user_endpoint(self, instance, search_string, auth=None):
        # Set rosolve=true to get better search results and perform authenticated search. Refer https://docs.joinmastodon.org/methods/search/
        # Alternatively, use accounts endpoint if needed. Refer https://docs.joinmastodon.org/methods/accounts/
        if auth != None:
            endpoint_url = f'{instance}/api/v2/search?q={search_string}&type=accounts&resolve=true'
            auth_token = 'Bearer ' + auth
            header = {'Authorization':auth_token}
            result = self.make_endpoint_request(endpoint_url, headers=header)
        else:
            endpoint_url = f'{instance}/api/v2/search?'
            params=urllib.parse.urlencode({'q': search_string,'type': 'accounts'})
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
            }
            http = httplib2.Http()
            url = endpoint_url + params
            response, content = http.request(url, "GET", headers=headers)
            result = json.loads(content.decode('utf-8'))

        user_data = []

        try:
            print('Results found for ' + instance)
            print(result['accounts'])
            for item in result['accounts']:
                user_id = item['id']
                user_name = item['username']
                display_name = item['display_name']
                is_bot = item['bot']
                user_followers_count = item['followers_count']
                user_following_count = item['following_count']
                user_statuses_count = item['statuses_count']

                entry = [instance, user_id, user_name, is_bot, display_name, user_followers_count, user_following_count, user_statuses_count]
                user_data.append(entry)
        except:
            print('No results found for ' + instance)
        
        return user_data

    
    def get_user_data(self, instances, user_lookup_string, auth=None):
        cols = ['instance', 'user_id', 'user_name', 'is_bot', 'display_name', 'user_followers_count', 'user_following_count', 'user_statuses_count']
        data = []

        for instance in instances:
            instance_data = self.user_lookup(instance, user_lookup_string, auth=auth)
            for result in instance_data:
                data.append(result)

        formatted_data = []
        for row in data:
            formatted_row = {cols[i]: row[i] for i in range(len(cols))}
            formatted_data.append(formatted_row)

        return formatted_data
    

    ## Status/Post Search ##
    def request_status_endpoint(self, instance, search_string, auth=None):
        # Set rosolve=true to get better search results and perform authenticated search. Refer https://docs.joinmastodon.org/methods/search/
        if auth != None:
            endpoint_url = f'{instance}/api/v2/search?q={search_string}&type=statuses&resolve=true'
            auth_token = 'Bearer ' + auth
            header = {'Authorization':auth_token}
            result = self.make_endpoint_request(endpoint_url, headers=header)
        else:
            endpoint_url = f'{instance}/api/v2/search?q={search_string}&type=statuses'
            result = self.make_endpoint_request(endpoint_url)

        search_data = []

        try:
            for item in result['statuses']:
                user_id = item['account']['id']
                user_name = item['account']['username']
                is_bot = item['account']['bot']
                post = item['content']
                url = item['uri']
                status_id = item['id']

                entry = [instance, user_id, user_name, is_bot, post, url, status_id]
                search_data.append(entry)
        except:
            print('no results found for ' + endpoint_url)
        
        return search_data
    
    def get_status_data(self, instances, post_query_string, auth=None):
        cols = ['instance', 'user_id', 'user_name', 'is_bot', 'post', 'url', 'status_id']
        data = []

        for instance in instances:
            instance_data = self.status_lookup(instance, post_query_string, auth=auth)
            for result in instance_data:
                data.append(result)

        formatted_data = []
        for row in data:
            formatted_row = {cols[i]: row[i] for i in range(len(cols))}
            formatted_data.append(formatted_row)

        return formatted_data
    

    ## Hashtag Search ##
    def request_hashtag_endpoint(self, instance, hashtag):
        endpoint_url = f'{instance}/api/v1/timelines/tag/{hashtag}'
        result = self.make_endpoint_request(endpoint_url)

        hashtag_data = []

        try:
            for item in result:
                user_id = item['account']['id']
                user_name = item['account']['username']
                is_bot = item['account']['bot']
                post = item['content']
                url = item['uri']
                status_id = item['id']

                entry = [instance, hashtag, user_id, user_name, is_bot, post, url, status_id]
                hashtag_data.append(entry)
        except:
            print('no results found for ' + endpoint_url)

        return hashtag_data
    
    def get_hashtag_data(self, instances, hashtag):
        cols = ['instance', 'hashtag', 'user_id', 'user_name', 'is_bot', 'post', 'url', 'status_id']
        data = []

        for instance in instances:
            instance_data = self.request_hashtag_endpoint(instance, hashtag)
            for result in instance_data:
                data.append(result)
        
        formatted_data = []
        for row in data:
            formatted_row = {cols[i]: row[i] for i in range(len(cols))}
            formatted_data.append(formatted_row)

        return formatted_data
    

    def get_top_instances(self, num_instances):
        instances = []
        PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print('PARENT_DIR')
        print(PARENT_DIR)
        with open(PARENT_DIR+'/data/mastodon_instance_info.txt') as f:
            instance_names = f.readlines()
            for i in range(0, num_instances):
                instances.append('https://'+instance_names[i].strip())
        
        return instances

    def search_instance_data(self, instance, search_string, type):
        instances = []
        data = []

        # get data from top 10 instances
        if instance == 'top10':
            instances = self.get_top_instances(10)
        # get data from top 25 instances
        elif instance == 'top25':
            instances = self.get_top_instances(25)
        # get data from specific instance
        else:
            instances.append('https://'+instance)

        if type == 'user':
            data = self.get_user_data(instances=instances, user_lookup_string=search_string)
        elif type == 'post':
            data = self.get_status_data(instances=instances, post_query_string=search_string)
        elif type == 'hashtag':
            data =self.get_hashtag_data(instances=instances, hashtag=search_string)
        
        return data