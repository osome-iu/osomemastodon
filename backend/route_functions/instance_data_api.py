"""
Purpose:
    This script used to add API endpoints to get the mastodon instance data
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
from mastoapp import capture_instances

blueprint = Blueprint('data_api', __name__, url_prefix='/api')

@blueprint.route('/get-instance-data', methods= ['GET'])
def get_instance_data():
    """
    Fetches all the mastodon instance data
    """
    try:
        mastodon_instances = capture_instances.fetch_instance_data()
    except:
        return "Bad request", 400
    else:
        return mastodon_instances

@blueprint.route('/get-instance-data-saved', methods= ['GET'])
def read_instance_data_saved():
    """
    Fetches all the mastodon instance data saved.
    """
    try:
        mastodon_instances = capture_instances.get_all_instance_from_saved_file()
    except:
        return "Bad request", 400
    else:
        return mastodon_instances
