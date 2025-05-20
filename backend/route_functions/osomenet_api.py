"""
Purpose:
    This script used to call the Mastodon data to feed into OSoMeNet Mastodon module.
Inputs:
    - Please update at the end.
Outputs:
    - Please update at the end.
Authors: Pasan Kamburugamuwa
"""

import os
import time
from flask import Blueprint,request,jsonify
from mastoapp import osomenet_search
from library import backend_util

# Define logger
logger = backend_util.get_logger(script_name=os.path.basename(__file__), also_print=True)

# Define blueprint
blueprint = Blueprint('osomenet_api', __name__, url_prefix='/api')

#########################################################
########### OSoMeNet API endpoints #####################
#########################################################

@blueprint.route('/get-public-timeline-hashtag-data', methods=['POST'])
def get_public_timeline_posts_by_hashtag():
    try:
        data = request.get_json()
        mastodon_instances = data.get('mstdn_instances', [])
        searched_hashtag = data.get('hashtag', '')
        limit = min(int(data.get('limit', 40)), 40)
        max_results = min(int(data.get('max_limit', 100)), 1000)
        is_diffusion_network = data.get("is_diffusion_network", False)

        logger.info(f"Collecting data for hashtag: {searched_hashtag} on instances: {mastodon_instances}")

        all_collected_data_list = []
        for mastodon_instance in mastodon_instances:
            if not mastodon_instance:
                continue

            since_id = None
            total_results = 0
            instance_results = []

            while total_results < max_results:
                hashtag_data = osomenet_search.public_timeline_search_by_hashtag(
                    mastodon_instance, searched_hashtag, limit, since_id
                )

                if not hashtag_data:
                    break

                # Add instance metadata
                for record in hashtag_data:
                    record['instance_name'] = mastodon_instance

                instance_results.extend(hashtag_data)
                total_results += len(hashtag_data)
                since_id = hashtag_data[-1]['id']

                if len(hashtag_data) < limit or total_results >= max_results:
                    break

                time.sleep(1)

            logger.info(f"Fetched {total_results} posts from {mastodon_instance}")
            all_collected_data_list.extend(instance_results[:max_results])

        if is_diffusion_network:
            all_collected_data_list = osomenet_search.retrieve_posts_replies_and_boosts(all_collected_data_list)

        return jsonify(all_collected_data_list)

    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        return jsonify({"error": "Bad request"}), 400

@blueprint.route('/get-posts-by-search-keyword', methods=['POST'])
def get_mstdn_search_keyword_posts():
    """
    Get posts for the searched keyword and return all statuses in a single array.
    """
    try:
        data = request.get_json()
        mastodon_instances = data.get('mastodon_instances')
        search_keyword = data.get('keyword')
        limit = data.get('limit') or 40
        max_limit = data.get('max_limit') or 100 # Use 100 if not provided max results
        is_diffusion_network = data.get("is_diffusion_network") or False
        all_statuses = []

        if not mastodon_instances or not search_keyword:
            logger.error("Missing mastodon instance or keyword")
            return jsonify({"error": "Missing mastodon_instances or keyword"}), 400

        logger.info(f"Start collecting data for Mastodon diffusion network for the keyword : {search_keyword} on {mastodon_instances} with limit {limit} and maximum limit {max_limit}")

        for instance in mastodon_instances:
            name = instance.get('name')
            access_token = instance.get('access_token')

            if not name or not access_token:
                logger.warning(f"Skipping instance due to missing name or access token: {instance}")
                continue

            # Perform the search
            data = osomenet_search.querynet_keyword_search(access_token, search_keyword, name, limit, int(max_limit))
            if data and data.get('statuses'):
                all_statuses.extend(data['statuses'])

        if is_diffusion_network:
            # Grab the replies and re-blogged accounts
            all_statuses = osomenet_search.retrieve_posts_replies_and_boosts(all_statuses)

        logger.info(f"End of retrieving Mastodon co-occurrence network with given hashtag")
        return jsonify(all_statuses)

    except Exception as e:
        logger.error(f"Error in QueryNet get posts by searched keyword: {e}")
        return jsonify({"error": str(e)}), 500

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
                timeline_status = osomenet_search.fetch_timeline_status_data(mastodon_instance_name, data_type, limit)
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
                hashtag_statuses = osomenet_search.fetch_hashtag_data(mastodon_instance_name, hashtag, data_type, limit_no)
                if 'statuses_timeline' in hashtag_statuses:
                    success_results.append(hashtag_statuses)
                if 'error_search_not_allowed' in hashtag_statuses:
                    error_in_results.append(mastodon_instance_name)
        hashtag_timeline_result_set.append({"timeline_status": success_results})
        hashtag_timeline_result_set.append({"error_search_not_allowed": error_in_results})
    except:
        return "Bad request", 400
    else:
        return jsonify(hashtag_timeline_result_set)
