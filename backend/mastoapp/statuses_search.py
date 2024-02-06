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
    - mastodon_instance - name of the mastodon instance
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
    status_endpoint_url = f'https://{mastodon_instance}/api/v1/statuses/{status_id}'
    response = requests.get(status_endpoint_url)
    status = response.json()
    return status


import requests


def mastodon_search_by_keyword(access_token, search_keyword, mastodon_instance):
    """
    This method is used to get the accounts, statuses, and hashtags.

    Parameters:
    - access_tokens - Bearer tokens to retrieve statuses
    - search_keyword - search keyword

    Returns:
    - JSON object
        "accounts": [...],
        "statuses": [...],
        "hashtags": [...]

    Note: Reference - https://docs.joinmastodon.org/methods/search/
    """
    search_endpoint_url = f'https://{mastodon_instance}/api/v2/search?q={search_keyword}&type=statuses&resolve=true'

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    try:
        response = requests.get(search_endpoint_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        if response.status_code == 200:
            status_data = response.json()
            searched_status = {"searched_status": status_data}

    except requests.exceptions.HTTPError as err:
        # Handle HTTP errors (4xx or 5xx) here
        searched_status = {"error_search_not_allowed": "Bad request (400 error)"}

    except Exception as e:
        # Handle other exceptions here
        searched_status = {"error_search_access_key_instances": f"An unexpected error occurred: {e}"}

    return searched_status
