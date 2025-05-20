from flask import Blueprint, request, jsonify
from mastoapp import interface_search

# Create a Blueprint for data API endpoints
blueprint = Blueprint('interface_api', __name__, url_prefix='/api')

#########################################################
########### Mastodon Instance Data Endpoints ############
#########################################################

@blueprint.route('/get-instance-data', methods=['GET'])
def get_instance_data():
    """
    Fetch current Mastodon instance data from the live source.

    Returns:
        JSON: Mastodon instance data if successful
        Tuple: Error message and 400 status code if request fails
    """
    try:
        mastodon_instances = interface_search.fetch_instance_data()
        return mastodon_instances
    except Exception as e:
        return f"Bad request: {str(e)}", 400


@blueprint.route('/get-instance-data-saved', methods=['GET'])
def read_instance_data_saved():
    """
    Fetch Mastodon instance data from the saved file.

    Returns:
        JSON: Saved Mastodon instance data if successful
        Tuple: Error message and 400 status code if request fails
    """
    try:
        mastodon_instances = interface_search.get_all_instance_from_saved_file()
        return mastodon_instances
    except Exception as e:
        return f"Bad request: {str(e)}", 400


#########################################################
####### Mastodon account search API endpoints ###########
#########################################################

@blueprint.route('/account-search-by-id', methods= ['GET'])
def search_account_data_by_id():
    """
    Search the account through account id
    """
    try:
        mastodon_instance = request.args.get('mastodon_instance')
        account_id = request.args.get('account_id')
        status = interface_search.fetch_account_data_by_account_id(mastodon_instance, account_id)
    except Exception as e:
        return f"Bad request: {str(e)}", 400
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
        error_in_results = []
        success_results = []
        for mastodon_instance in mastodon_instances:
            mastodon_instance_name = mastodon_instance.get('name')
            if mastodon_instance_name:
                hashtag_data = interface_search.get_account_data_from_keyword(mastodon_instance_name, search_keyword)
                if 'results' in hashtag_data:
                    for account in hashtag_data['results']['accounts']:
                        account['instance_name'] = mastodon_instance_name  # Add instance name to each account
                    success_results.extend(hashtag_data['results']['accounts'])
                if 'error_search_not_allowed' in hashtag_data:
                    error_in_results.append(mastodon_instance_name)
        account_result_set.append({"searched_accounts": success_results})
        account_result_set.append({"error_search_not_allowed": error_in_results})
    except Exception as e:
        return f"Bad request: {str(e)}", 400
    return jsonify(account_result_set)

#########################################################
####### Mastodon statuses search API endpoints ##########
#########################################################

@blueprint.route('/search-status-by-id', methods= ['GET'])
def search_status_data_by_id():
    """
    Search the status through the status id.
    """
    try:
        mastodon_instance = request.args.get('mastodon_instance')
        status_id = request.args.get('status_id')
        status = interface_search.status_search_by_id(mastodon_instance, status_id)
    except Exception as e:
        return f"Bad request: {str(e)}", 400
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
                status_data = interface_search.mastodon_search_by_keyword(access_token, search_keyword, mastodon_instance_name)
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
    except Exception as e:
        return f"Bad request: {str(e)}", 400
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
                hashtag_data = interface_search.get_hashtag_data_from_keyword(mastodon_instance_name, search_keyword)
                if 'results' in hashtag_data:
                    success_results.extend(hashtag_data['results']['hashtags'])
                if 'error_search_not_allowed' in hashtag_data:
                    error_in_results.append(mastodon_instance_name)
        hashtag_result_set.append({"searched_status": success_results})
        hashtag_result_set.append({"error_search_not_allowed": error_in_results})
    except Exception as e:
        return f"Bad request: {str(e)}", 400
    else:
        return jsonify(hashtag_result_set)

#########################################################
####### Mastodon status timeline search endpoints #######
#########################################################

@blueprint.route('/timeline-statuses', methods= ['POST'])
def get_statuses_timeline_data():
    """
    Get the timeline statuses
    """
    try:
        data = request.get_json()
        mastodon_instances = data.get('mastodon_instances')
        data_type = data.get('data_type')
        limit = data.get('limit_no')
        statuses_timeline_result_set = []
        success_results = []
        error_in_results = []
        for mastodon_instance in mastodon_instances:
            mastodon_instance_name = mastodon_instance.get('name')
            if mastodon_instance_name:
                timeline_status = interface_search.fetch_timeline_status_data(mastodon_instance_name, data_type, limit)
                if 'statuses_timeline' in timeline_status:
                    success_results.append(timeline_status)
                if 'error_search_not_allowed' in timeline_status:
                    error_in_results.append(mastodon_instance_name)
        statuses_timeline_result_set.append({"timeline_status": success_results})
        statuses_timeline_result_set.append({"error_search_not_allowed": error_in_results})
    except Exception as e:
        return f"Bad request: {str(e)}", 400
    else:
        return jsonify(statuses_timeline_result_set)

@blueprint.route('/hashtag-search', methods= ['POST'])
def search_timeline_hashtag_by_statuses():
    """
    Search the statuses through hashtag search.
    """
    try:
        data = request.get_json()
        mastodon_instances = data.get('mastodon_instances')
        hashtag = data.get('hashtag')
        data_type = data.get('data_type')
        limit_no = data.get('limit_no')
        hashtag_timeline_result_set = []
        success_results = []
        error_in_results = []

        for mastodon_instance in mastodon_instances:
            mastodon_instance_name = mastodon_instance.get('name')
            if mastodon_instance_name:
                hashtag_statuses = interface_search.fetch_hashtag_data(mastodon_instance_name, hashtag, data_type, limit_no)
                if 'statuses_timeline' in hashtag_statuses:
                    success_results.append(hashtag_statuses)
                if 'error_search_not_allowed' in hashtag_statuses:
                    error_in_results.append(mastodon_instance_name)
        hashtag_timeline_result_set.append({"timeline_status": success_results})
        hashtag_timeline_result_set.append({"error_search_not_allowed": error_in_results})
    except Exception as e:
        return f"Bad request: {str(e)}", 400
    else:
        return jsonify(hashtag_timeline_result_set)
