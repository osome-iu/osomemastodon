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
from mastoapp import capture_instances
from mastodon import Mastodon, StreamListener
import psycopg2

# Log file location and the file
LOG_DIR = "/home/data/apps/mastodon/log"
LOG_FNAME = "mastodon_logging.log"

# Add mastodon app to path
PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(PARENT_DIR, "mastoapp"))
from mastodon_search import MastodonSearch
from capture_instances import CaptureMastodonInstances
from mastodon_streamer import mastodonStreamer
import threading

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

ms = MastodonSearch()
ci = CaptureMastodonInstances()

@app.route('/instances', methods=['GET'])
@cross_origin()
def get_domains():
    instances = []
    instances.append('top10')
    instances.append('top25')
    with open(PARENT_DIR+'/data/mastodon_instance_info.txt') as f:
        instance_names = f.readlines()
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
    data = ms.search_instance_data(instance, search_string, search_type)
    return jsonify(data)

if __name__ == '__main__':
    LOG_DIR = "/Users/pkamburu/IUNI/mastodon/osomemastodon/backend/log"
    LOG_FNAME = "mastodon_logging.log"

    # Create logger
    script_name = os.path.basename(__file__)
    logger = backend_util.get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)
    logger.info("-" * 50)
    logger.info(f"Begin script: {__file__}")

    # Define the instance names and stream methods for public and local streams
    instances_and_streams = [
        {'instance_name': 'https://mastodon.social', 'stream_method': 'public', 'access_token' : 'LDqotkJzIDexTZ56ASuz23kO50YmMYhI5Ojt2cuapcE'},
        {'instance_name': 'https://mastodon.cloud', 'stream_method': 'public', 'access_token' : 'Jo4ykUA2i56eBWuk0J_sHJ7_TVVU0_4JmzUQimXwokk'},
        {'instance_name': 'https://mastodon.social', 'stream_method': 'local', 'access_token' : 'LDqotkJzIDexTZ56ASuz23kO50YmMYhI5Ojt2cuapcE'},
        {'instance_name': 'https://mastodon.cloud', 'stream_method': 'local', 'access_token' : 'Jo4ykUA2i56eBWuk0J_sHJ7_TVVU0_4JmzUQimXwokk'}
    ]

    # Create threads and start streaming for each instance and stream method
    threads = []
    for instance_info in instances_and_streams:
        thread = threading.Thread(target=mastodonStreamer.stream_data, args=(instance_info,))
        threads.append(thread)

    try:
        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        logger.info("Keyboard interrupt detected. Stopping threads...")
        for thread in threads:
            thread.join()

    finally:
        # Fetch instance data after the threads are finished or interrupted
        ci.fetch_instance_data()

    app.run(host=backend_util.get_flask_host(), port=int(backend_util.get_flask_port()), debug=backend_util.get_flask_debug_mode())
