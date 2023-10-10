"""
Purpose:
    This script used to search the hashtag data from the mastodon API.
Inputs:
    - The data need to be passed from the function
       |- hashtag, data_type(public, local), limit
    None
Outputs:
    None
Authors: Pasan Kamburugamuwa
"""


from flask import Blueprint,request
from mastoapp import hashtag_search

blueprint = Blueprint('hashtag_api', __name__, url_prefix='/api')

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