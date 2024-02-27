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


from flask import Blueprint,request,jsonify
from mastoapp import timeline_statuses,hashtag_search

blueprint = Blueprint('timeline_api', __name__, url_prefix='/api')

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
                timeline_status = timeline_statuses.fetch_timeline_status_data(mastodon_instance_name, data_type, limit)
                if 'statuses_timeline' in timeline_status:
                    success_results.append(timeline_status)
                if 'error_search_not_allowed' in timeline_status:
                    error_in_results.append(mastodon_instance_name)
        statuses_timeline_result_set.append({"timeline_status": success_results})
        statuses_timeline_result_set.append({"error_search_not_allowed": error_in_results})
    except:
        return "Bad request", 400
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
                hashtag_statuses = hashtag_search.fetch_hashtag_data(mastodon_instance_name, hashtag, data_type, limit_no)
                if 'statuses_timeline' in hashtag_statuses:
                    success_results.append(hashtag_statuses)
                if 'error_search_not_allowed' in hashtag_statuses:
                    error_in_results.append(mastodon_instance_name)
        hashtag_timeline_result_set.append({"timeline_status": success_results})
        hashtag_timeline_result_set.append({"error_search_not_allowed": error_in_results})
    except:
        return "Bad request", 400
    else:
        print(hashtag_timeline_result_set)
        return jsonify(hashtag_timeline_result_set)