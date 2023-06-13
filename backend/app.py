from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import os, sys
# Add mastoapp to path
PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(PARENT_DIR, "mastoapp"))
from mastodon_search import MastodonSearch

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

ms = MastodonSearch()

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
    app.run(host="127.0.0.1", debug=True, port=7000)
