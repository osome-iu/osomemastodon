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
def get_fib_indices():
    """
    Fetches all the mastodon instance data
    """
    try:
        mastodon_instances = capture_instances.fetch_instance_data()
        print(mastodon_instances)
    except:
        return "Bad request", 400
    else:
        return mastodon_instances
