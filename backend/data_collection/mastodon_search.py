import requests
import json
from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)

def mastodon_search(access_token, search_keyword, search_type):
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
    https://docs.joinmastodon.org/methods/search/
    """
    if search_type == 'all':
        search_endpoint_url = f'https://mastodon.social/api/v2/search?q={search_keyword}&limit=10000'
    else:
        search_endpoint_url = f'https://mastodon.social/api/v2/search?q={search_keyword}&type={search_type}&limit=10000'

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

#Search the status from a keyword
@app.route('/searchstatus', methods=['GET'])
@cross_origin()
def search_status():
    access_token = request.args.get('access_token')
    search_keyword = request.args.get('search_keyword')
    search_type = request.args.get('search_type')
    json_data = mastodon_search(access_token,search_keyword,search_type)
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(host='localhost', port=8093,debug=True)