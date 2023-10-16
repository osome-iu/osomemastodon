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


from flask import Blueprint,request
from mastoapp import capture_instances,statuses_search

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