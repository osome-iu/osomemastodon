import requests
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import httplib2
import urllib.parse
import os, sys
from flask import Flask, request, jsonify, Response

app = Flask(__name__)


def status_search_by_id(mastodon_instance, status_id):
    """
    This method is used to search the statuses from status's id

    Parameters passing
    -----------
    - status_id - status_id

    Returns
    - JSON object
        {
            "id": "1",
            "created_at": "2016-03-16T14:44:31.580Z",
            "in_reply_to_id": null,
            "in_reply_to_account_id": null,
            "sensitive": false,
            "spoiler_text": "",
            "visibility": "public",
            "language": "en",
            "uri": "https://mastodon.social/users/Gargron/statuses/1",
            "url": "https://mastodon.social/@Gargron/1",
            "replies_count": 7
            ...
        }
        -----------
    """
    status_endpoint_url = f'{mastodon_instance}/api/v1/statuses/{status_id}'
    response = requests.get(status_endpoint_url)
    status = response.json()
    return status


def mastodon_search_by_keyword(access_token, search_keyword, search_type, mastodon_instance):
    """
    This method is used to get the accounts,statuses and hashtags.

    Parameters passing
    -----------
    - access_token - Bearer token to retrieve statuses
    - q - query_search

    Returns
    - JSON object
        "accounts": [
            ...
            ],
            "statuses":[
            ...
            ],
            "hashtags":[
            ...
            ],
    -----------
    Note: here is the reference : https://docs.joinmastodon.org/methods/search/
    """
    if search_type == 'all':
        search_endpoint_url = f'https://{mastodon_instance}/api/v2/search?q={search_keyword}'
        print(search_endpoint_url)
    else:
        search_endpoint_url = f'https://{mastodon_instance}/api/v2/search?q={search_keyword}&type={search_type}'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(search_endpoint_url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        status = response.json()
        return status
    else:
        # Handle the errors occur with API method calling.
        print(f"Error: {response.status_code} - {response.text}")
