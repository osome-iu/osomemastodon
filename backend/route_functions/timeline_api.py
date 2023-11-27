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
        for mastodon_instance in mastodon_instances:
            for key, instance_name in mastodon_instance.items():
                if key == 'name':
                    timeline_status = timeline_statuses.fetch_timeline_status_data(instance_name, data_type, limit)
                    statuses_timeline_result_set.append(timeline_status)
    except:
        return "Bad request", 400
    else:
        print(statuses_timeline_result_set)
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
        for mastodon_instance in mastodon_instances:
            for key, instance_name in mastodon_instance.items():
                if key == 'name':
                    hashtag_statuses = hashtag_search.fetch_hashtag_data(instance_name, hashtag, data_type, limit_no)
                    hashtag_timeline_result_set.append(hashtag_statuses)
    except:
        return "Bad request", 400
    else:
        return jsonify(hashtag_timeline_result_set)