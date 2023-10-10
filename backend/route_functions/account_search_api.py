"""
Purpose:
    This script used to search the account details through the mastodon account API.
Inputs:
    - The data need to be passed from the function
       |- account_id, mastodon_instance
    None
Outputs:
    A
    None
Authors: Pasan Kamburugamuwa
"""


from flask import Blueprint,request
from mastoapp import account_search

blueprint = Blueprint('account_api', __name__, url_prefix='/api')

@blueprint.route('/account-search-by-id', methods= ['GET'])
def search_account_data_by_id():
    """
    Search the account through account id
    """
    try:
        mastodon_instance = request.args.get('mastodon_instance')
        account_id = request.args.get('account_id')
        status = account_search.fetch_account_data(mastodon_instance, account_id)
    except:
        return "Bad request", 400
    else:
        return status
