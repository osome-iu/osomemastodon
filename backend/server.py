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
from flask import Flask, request, jsonify, Response, render_template
from flask_cors import CORS, cross_origin
import os, sys
from library import backend_util
from route_functions import instance_data_api, search_api,account_search_api,timeline_api

# Log file location and the file
LOG_DIR = "/Users/pkamburu/IUNI/mastodon/backup/untitledfolder2/log"
LOG_FNAME = "mastodon_logging.log"

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

#render the frontend
@app.route('/')
@cross_origin()
def index():
    resp = render_template("/index.html")
    return resp

@app.route('/<path:fallback>')
@cross_origin()
def index_fallback(fallback):
    resp = render_template("/index.html")
    return resp

# register blueprints
app.register_blueprint(instance_data_api.blueprint)
app.register_blueprint(search_api.blueprint)
app.register_blueprint(account_search_api.blueprint)
app.register_blueprint(timeline_api.blueprint)

if __name__ == '__main__':
    script_name = os.path.basename(__file__)
    logger = backend_util.get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)
    logger.info("-" * 50)
    logger.info(f"Begin script: {__file__}")
    app.run(host=backend_util.get_flask_host(), port=int(backend_util.get_flask_port()), debug=backend_util.get_flask_debug_mode())
