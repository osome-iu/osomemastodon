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


from flask import Blueprint,request,jsonify
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

@blueprint.route('/search-accounts-by-keyword', methods= ['POST'])
def search_account_data_by_keyword():
    """
    Search the hashtag data through hashtag keyword.
    """
    try:
        data = request.get_json()
        mastodon_instances = data.get('instances')
        search_keyword = data.get('keyword')
        account_result_set = []
        for mastodon_instance in mastodon_instances:
            for key, instance_name in mastodon_instance.items():
                if key == 'name':
                    account_data = account_search.get_account_data_from_keyword(instance_name, search_keyword)
                    account_result_set.append(account_data)
    except:
        return "Bad request", 400
    else:
        return jsonify(account_result_set)
