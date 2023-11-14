"""
Purpose:
    This script used to search statuses through a keyword and search through the status ID
Inputs:
    - The data need to be passed from the function
       |- report_date,platform, user_id
    None
Outputs:
    A
    None
Authors: Pasan Kamburugamuwa
"""


from flask import Blueprint,request,jsonify
from mastoapp import capture_instances,statuses_search, hashtag_search

blueprint = Blueprint('status_api', __name__, url_prefix='/api')

@blueprint.route('/search-status-by-id', methods= ['GET'])
def search_status_data_by_id():
    """
    Search the status through the status id.
    """
    try:
        mastodon_instance = request.args.get('mastodon_instance')
        status_id = request.args.get('status_id')
        status = statuses_search.status_search_by_id(mastodon_instance, status_id)
    except:
        return "Bad request", 400
    else:
        return status

@blueprint.route('/search-status-by-keyword', methods= ['GET'])
def search_status_data_by_keyword():
    """
    Search the status through the status id.
    """
    try:
        mastodon_instance = request.args.get('mastodon_instance')
        search_keyword = request.args.get('keyword')
        search_type = request.args.get('type')
        client_key = request.args.get('client_key')
        status = statuses_search.mastodon_search_by_keyword(client_key, search_keyword, search_type, mastodon_instance)
    except:
        return "Bad request", 400
    else:
        return status


@blueprint.route('/search-hashtag-by-keyword', methods= ['POST'])
def search_hashtag_data_by_keyword():
    """
    Search the hashtag data through hashtag keyword.
    """
    try:
        data = request.get_json()
        mastodon_instances = data.get('instances')
        search_keyword = data.get('keyword')
        hashtag_result_set = []
        for mastodon_instance in mastodon_instances:
            for key, value in mastodon_instance.items():
                if key == 'name':
                    hashtag_data = hashtag_search.get_hashtag_data_from_keyword(value, search_keyword)
                    hashtag_result_set.append(hashtag_data)
    except:
        return "Bad request", 400
    else:
        return jsonify(hashtag_result_set)