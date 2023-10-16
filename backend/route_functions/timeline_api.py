"""
Purpose:
    This script used to get the timeline statuses and hashtag statuses
Inputs:
    - The data need to be passed from the function
       |- hashtag, data_type(public, local), limit
    None
Outputs:
    None
Authors: Pasan Kamburugamuwa
"""


from flask import Blueprint,request
from mastoapp import timeline_statuses,hashtag_search

blueprint = Blueprint('timeline_api', __name__, url_prefix='/api')

@blueprint.route('/timeline-statuses', methods= ['GET'])
def get_statuses_timeline_data():
    """
    Get the timeline statuses
    """
    try:
        mastodon_instance = request.args.get('mastodon_instance')
        data_type = request.args.get('data_type')
        limit = request.args.get('limit')
        timeline_status = timeline_statuses.fetch_timeline_status_data(mastodon_instance, data_type, limit)
    except:
        return "Bad request", 400
    else:
        return timeline_status

@blueprint.route('/hashtag-search', methods= ['GET'])
def search_account_data_by_id():
    """
    Search the statuses through hashtag search.
    """
    try:
        mastodon_instance = request.args.get('mastodon_instance')
        hashtag = request.args.get('hashtag')
        data_type = request.args.get('data_type')
        limit = request.args.get('limit')
        hashtag_statuses = hashtag_search.fetch_hashtag_data(mastodon_instance, hashtag, data_type, limit)
    except:
        return "Bad request", 400
    else:
        return hashtag_statuses