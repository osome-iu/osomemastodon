from library import backend_util, network

test_data_path = '/Users/pkamburu/Mastodon/MastodonInterface/osomemastodon/backend/test/test_data.json'

def test_network():
    with open(test_data_path, 'r') as f:
        data = json.load(f)
    print(data)

test_network()