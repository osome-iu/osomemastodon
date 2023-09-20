import requests
import json
from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
def status_search(status_id):
    """
    This method is used to get the status by passing status id

    Parameters passing
    -----------
    - status_id - status_id

    Returns
    - JSON object
        {
            "account": {
            },
            "application": {
            },
            "card": null,
            "content": "<p>this is the stray cat that comes..</p>",
            "created_at": "2023-08-07T00:00:55.733Z",
            "edited_at": null,
            "emojis": [],
            "favourites_count": 1,
            "id": "110845392042833405",
            "in_reply_to_account_id": null,
            "in_reply_to_id": null,
            "media_attachments": [{
                }
            ],
            "mentions": [],
            "poll": null,
            "reblog": null,
            "reblogs_count": 0,
            "replies_count": 0,
            "sensitive": false,
            "spoiler_text": "",
            "tags": [],
            "uri": "https://mastodon.social/users/w0mp/statuses/110845392042833405",
            "url": "https://mastodon.social/@w0mp/110845392042833405",
            "visibility": "public
           ...
        }
    -----------
    """
    status_endpoint_url = f'https://mastodon.social/api/v1/statuses/{status_id}'
    response = requests.get(status_endpoint_url)
    status = response.json()
    return status

#Search the status from status_id
@app.route('/searchstatus', methods=['GET'])
@cross_origin()
def search_status():
    status_id =  request.args.get('status_id')
    json_data = status_search(status_id)
    return jsonify(json_data)

# Example status Id's - 110845394784266982, 110845394814656087, 110845394920312712, 110845390995484737, 110845392572914054, 110845392682144438
# search method : http://localhost:8092/searchstatus?status_id=110845390995484737

if __name__ == '__main__':
    app.run(host='localhost', port=8092,debug=True)