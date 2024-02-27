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

@blueprint.route('/search-status-by-keyword', methods=['POST'])
def search_status_data_by_keyword():
    """
    Search the status through the status keyword.
    """
    try:
        data = request.get_json()
        mastodon_instances = data.get('mastodon_instances')
        access_tokens = data.get('access_tokens')
        search_keyword = data.get('keyword')

        mastodon_instance_list = [{'name': instance['name'], 'access_token': token} for instance, token in
                                  zip(mastodon_instances, access_tokens)]

        statuses_result_set = []
        search_success_array = []
        search_not_allowed_error_array = []
        search_access_key_error_array = []

        combined_status_data = []  # Initialize here

        for mastodon_instance in mastodon_instance_list:
            mastodon_instance_name = mastodon_instance.get('name')
            access_token = mastodon_instance.get('access_token')
            if mastodon_instance_name and access_token:
                status_data = statuses_search.mastodon_search_by_keyword(access_token, search_keyword, mastodon_instance_name)
                if 'results' in status_data:
                    combined_status_data.extend(status_data['results']['statuses'])
                if 'error_search_not_allowed' in status_data:
                    search_not_allowed_error_array.append(mastodon_instance_name)
                if 'error_search_access_key' in status_data:
                    search_access_key_error_array.append(mastodon_instance_name)
                if 'searched_status_array' in status_data:
                    search_success_array.append(mastodon_instance_name)

        statuses_result_set.append({"searched_status": combined_status_data})
        statuses_result_set.append({'searched_status_array': search_success_array})
        statuses_result_set.append({'error_search_not_allowed': search_not_allowed_error_array})
        statuses_result_set.append({'error_search_access_key': search_access_key_error_array})
    except:
        return "Bad request", 400
    else:
        return jsonify(statuses_result_set)




@blueprint.route('/search-hashtag-by-keyword', methods= ['POST'])
def search_hashtag_data_by_keyword():
    """
    Hashtags - metadata
    Search the hashtag data through hashtag keyword.
    """
    try:
        data = request.get_json()
        mastodon_instances = data.get('instances')
        search_keyword = data.get('keyword')
        hashtag_result_set = []
        error_in_results = []
        success_results = []
        for mastodon_instance in mastodon_instances:
            mastodon_instance_name = mastodon_instance.get('name')
            if mastodon_instance_name:
                hashtag_data = hashtag_search.get_hashtag_data_from_keyword(mastodon_instance_name, search_keyword)
                if 'results' in hashtag_data:
                    success_results.extend(hashtag_data['results']['hashtags'])
                if 'error_search_not_allowed' in hashtag_data:
                    error_in_results.append(mastodon_instance_name)
        hashtag_result_set.append({"searched_status": success_results})
        hashtag_result_set.append({"error_search_not_allowed": error_in_results})
    except:
        return "Bad request", 400
    else:
        return jsonify(hashtag_result_set)