"""
Purpose:
    This script used to add API endpoints to get the mastodon instances and search the posts.
Inputs:
    - end points - /instances -> this will fetch the instances.
                 - /search -> search by a name. this will fetch all the posts related to this.
Outputs:
    - JSON object
Authors: Rishab Ravi and Pasan Kamburugamuwa
"""
from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import os, sys
from library import backend_util
import psycopg2

# Log file location and the file
LOG_DIR = "/Users/pkamburu/iuni/mastodon/logs"
LOG_FNAME = "mastodon_logging.log"

# Add mastodon app to path
PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(PARENT_DIR, "mastoapp"))
from mastodon_status_search import MastodonSearch
from capture_instances import CaptureMastodonInstances
from statuses_search import StatusSearch

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

ms = MastodonSearch()
ci = CaptureMastodonInstances()
ss = StatusSearch()

@app.route('/instances', methods=['GET'])
@cross_origin()
def get_domains():
    instances = []
    instances.append('top10')
    instances.append('top25')
    with open(PARENT_DIR+'/data/mastodon_instance_info.txt') as f:
        instance_names = f.readlines()
        print(instance_names)
        for row in instance_names:
            instances.append(row.strip())
    return jsonify(instances)

@app.route('/search', methods=['POST'])
@cross_origin()
def search():
    data = request.get_json()
    instance = data.get('instance')
    search_string = data.get('search_string')
    search_type = data.get('search_type')
    data = ss.search_instance_data(instance, search_string, search_type)
    return jsonify(data)

@app.route('/searchstatus', methods=['GET'])
@cross_origin()
def search_status():
    status_id =  request.args.get('status_id')
    json_data = ss.status_search(status_id)
    print(json_data)
    return jsonify(json_data)

#Search the status from a keyword
@app.route('/searchstatus', methods=['GET'])
@cross_origin()
def search_status():
    access_token = request.args.get('access_token')
    search_keyword = request.args.get('search_keyword')
    search_type = request.args.get('search_type')
    json_data = ms.mastodon_search(access_token,search_keyword,search_type)
    return jsonify(json_data)

if __name__ == '__main__':
    script_name = os.path.basename(__file__)
    logger = backend_util.get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)
    logger.info("-" * 50)
    logger.info(f"Begin script: {__file__}")
    ci.fetch_instance_data()
    app.run(host=backend_util.get_flask_host(), port=int(backend_util.get_flask_port()),debug=backend_util.get_flask_debug_mode())