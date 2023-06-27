import requests
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import httplib2
import urllib.parse
import os, sys
from database_functions import users, posts
from flask import Flask, request, jsonify, Response

app = Flask(__name__)
class MastodonSearch:
    def __init__(self):
        self.session = requests.Session()
        retry = Retry(connect=2, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.session.timeout = 5

    def make_endpoint_request(self, endpoint_url, headers=None):
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
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',}
            http = httplib2.Http()
            url = endpoint_url + params
            response, content = http.request(url, "GET", headers=headers)
            result = json.loads(content.decode('utf-8'))

        user_data = []

        try:
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

    
    def post_user_data(self, instances, user_lookup_string):
        """
        This API is used to get the user timeline data for the

        Parameters
        -----------
        - instance - instance name
        - user_lookup_string - user lookup string to search through the API

        Returns
        - id - id of the post
        - created_at - post creation timeline
        - visibility - visibility of the post
        - content - content of the post(html)
        - tags - tags of the post
        -----------
        """
        users_data_retrieved = []
        for instance in instances:
            formated_lookup_string = '@'+user_lookup_string+'@'+instance.replace("https://", "")
            user_data = self.user_lookup(instance, formated_lookup_string)
            if(user_data == None):
                return users_data_retrieved
            else:
                if users.check_user_already_exist(user_data['id']):
                    users.update_existing_user(
                        instance,
                        user_data['username'],
                        user_data['acct'],
                        user_data['display_name'],
                        user_data['locked'],
                        user_data['bot'],
                        user_data['created_at'],
                        user_data['avatar'],
                        user_data['followers_count'],
                        user_data['following_count'],
                        user_data['statuses_count'],
                        user_data['last_status_at'],
                        user_data['id']
                    )
                else:
                    users.add_users(
                        user_data['id'],
                        instance,
                        user_data['username'],
                        user_data['acct'],
                        user_data['display_name'],
                        user_data['locked'],
                        user_data['bot'],
                        user_data['created_at'],
                        user_data['avatar'],
                        user_data['followers_count'],
                        user_data['following_count'],
                        user_data['statuses_count'],
                        user_data['last_status_at']
                        )
                users_data_retrieved = users.get_user_data(user_data['id'])
                print(users_data_retrieved)
        return users_data_retrieved


    def user_lookup(self, instance, acct):
        """
        This method is used to get the mastodon account id when pass the account name.

        Parameters
        -----------
        - instance - instance name
        - user_lookup_string - user account name to pass to the API call

        Returns
        - JSON object
            - id : account_id
            - username : username of the mastodon user(ex- jrashf)
            - acct - account name(this will include both the username and the instance) ex-jrashf@mastodonapp.uk
            - display_name - Display name of the user (ex-jrashf@mastodonapp.uk)
            - locked - Is the account locked or not. (visibility)
            - bot - is it a bot(True or False)
            - discoverable - discoverable or not (True or False)
            - created_at - Account created date
            - avatar - Avatar Image
            - followers_count - No of followers have
            - following_count - No of following users the user has
            - statuses_count - No of posts
            - last_status_at - Last post created
        -----------
        Note - For all the above details we need only the account_id for up now.
        """
        user = {}
        user_lookup_endpoint_url = f'{instance}/api/v1/accounts/lookup'
        params = {
            'acct': acct
        }
        r = requests.get(user_lookup_endpoint_url, params=params)
        user = json.loads(r.text)

        if 'error' in user:
            # User not found, handle the error
            return None

        return user

    # api_url = f'{instance_url}/api/v2/search?q={keyword}'
    # headers = {'Authorization': f'Bearer {access_token}'}
    # response = requests.get(api_url, headers=headers)

    ## Post Search ##
    def request_status_endpoint(self, instance, search_string, auth=None):
        """
        View public statuses containing the given post search.

        Parameters
        -----------
        - instance: instance name
        - search_string: post search keyword.

        Returns
        - id: id of the post
        - created_at: post creation timeline
        - visibility: visibility of the post
        - content: content of the post (HTML)
        - tags: tags of the post
        -----------
        """
        if auth is not None:
            endpoint_url = f'{instance}/api/v2/search?q={search_string}&type=statuses&resolve=true'
            auth_token = 'Bearer ' + auth
            header = {'Authorization': auth_token}
            result = self.make_endpoint_request(endpoint_url, headers=header)
        else:
            endpoint_url = f'{instance}/api/v2/search?q={search_string}&type=statuses'
            result = self.make_endpoint_request(endpoint_url)
        print(result)
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
                add_post = posts.add_posts(status_id, instance, user_id, user_name, is_bot,post,url)
        except:
            print('no results found for ' + endpoint_url)
        return search_data

    ## Post Search ##
    def get_status_data(self, instances, post_query_string, auth=None):
        cols = ['instance', 'user_id', 'user_name', 'is_bot', 'post', 'url', 'status_id']
        data = []

        for instance in instances:
            instance_data = self.request_status_endpoint(instance, post_query_string, auth=auth)
            for result in instance_data:
                data.append(result)

        formatted_data = []
        for row in data:
            formatted_row = {cols[i]: row[i] for i in range(len(cols))}
            formatted_data.append(formatted_row)

        return formatted_data


    # Hashtag Search #
    def request_hashtag_endpoint(self, instance, hashtag):
        """
        View public statuses containing the given hashtag.

        Parameters
        -----------
        - instance - instance name
        - hashtag - name of the hashtag(not including the # symbol)

        Returns
        - id - id of the post
        - created_at - post creation timeline
        - visibility - visibility of the post
        - content - content of the post(html)
        - tags - tags of the post
        -----------
        """
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
        """
        This function is used to get top instances by reading the already stored data file

        Parameters
        -----------
        - num_instance - No of instance (25, 10 or 1)

        Returns
        - instances - Array
        -----------
        """
        instances = []
        PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(PARENT_DIR+'/data/mastodon_instance_info.txt') as f:
            instance_names = f.readlines()
            for i in range(0, num_instances):
                instances.append('https://'+instance_names[i].strip())
        
        return instances



    def search_instance_data(self, instance, search_string, type):
        """
        This function is used to get the instance data and search string to feed to user, post and hashtag functions

        Parameters
        -----------
        - instance - instance name
        - search_string - name of the search keyword.

        Returns
        - data - depend on the user search it will vary with user, post and hashtag.
        -----------
        """
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
            instances.append('https://' + instance)
        if type == 'user':
            data = self.post_user_data(instances=instances, user_lookup_string=search_string)
        elif type == 'post':
            data = self.get_status_data(instances=instances, post_query_string=search_string)
        elif type == 'hashtag':
            data =self.get_hashtag_data(instances=instances, hashtag=search_string)
        return data