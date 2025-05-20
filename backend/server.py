"""
Flask API server for Mastodon data with two main endpoints:
1. /api/instances - Get Mastodon instances data
2. /api/search - Search Mastodon posts

Also serves a frontend Vue/React app.
Authors: Rishab Ravi, Pasan Kamburugamuwa
"""

import os
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from library import backend_util
from route_functions import interface_api, osomenet_api

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Frontend routes
@app.route('/')
@app.route('/<path:fallback>')
@cross_origin()
def index(fallback=None):
    return render_template("/index.html")

# Register API blueprints
app.register_blueprint(interface_api.blueprint)
app.register_blueprint(osomenet_api.blueprint)

if __name__ == '__main__':
    logger = backend_util.get_logger(script_name=os.path.basename(__file__), also_print=True)
    logger.info(f"Starting server on {backend_util.get_flask_host()}:{backend_util.get_flask_port()}")
    app.run(
        host=backend_util.get_flask_host(),
        port=int(backend_util.get_flask_port()),
        debug=backend_util.get_flask_debug_mode()
    )