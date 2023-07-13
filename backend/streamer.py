import json
import os
import datetime
from mastodon import Mastodon, StreamListener
from library import backend_util

LOG_DIR = "/Users/pkamburu/iuni/mastodon/osomemastodon/backend"

"""
This script is used to write the post data of Mastodon social into mastdonsocial json.

Parameters
-----------
- Pass the instance social media key (get it from mastodon.social instance)
- Pass the instance url

Returns
- content - this would be html with having content
- username - username of the each account
- status_id - status_id
- created_at - post created_at
- visibility - visibility of the post
- post_url - url of the post.
-----------
"""

#initially count the post as 0
#initially the count the file size as 0
#initially the count the posts per day as 0
post_data = {
    'POST_COUNT': 0,
    'FILE_SIZE': 0,
    'post_count_per_day': {}
}

# Create a Mastodon client instance
mastodon = Mastodon(
    access_token='LDqotkJzIDexTZ56ASuz23kO50YmMYhI5Ojt2cuapcE',
    api_base_url='https://mastodon.social'
)

# Define a custom stream listener
class MyStreamListener(StreamListener):
    def on_update(self, status):
        # Increment post count
        post_data['POST_COUNT'] +=1

        # Get current date
        current_date = datetime.datetime.now().date()

        # Increment count for current date
        if current_date in post_data['post_count_per_day']:
            post_data['post_count_per_day'][current_date] += 1
        else:
            post_data['post_count_per_day'][current_date] = 1

        # Handle new toot
        toot_info = {
            'content': status['content'],
            'username': status['account']['username'],
            'status_id': status['id'],
            'created_at': status['created_at'],
            'visibility': status['visibility'],
            'post_url': status['url']
        }

        # Get current date
        current_date = datetime.datetime.now().date()
        file_name = f"mastdonsocial_{current_date}.json"

        # Calculate file size
        post_data['FILE_SIZE'] = os.path.getsize(f"mastdonsocial_{current_date}.json")\

        # Write toot info to JSON file
        with open(file_name, 'a') as file:
            json.dump(toot_info, file, default=str)
            file.write('\n')


# Get current date
current_date = datetime.datetime.now().date()
# Log file location and the file
LOG_FNAME = f"mastdonsocial_{current_date}.log"
script_name = os.path.basename(__file__)

logger = backend_util.get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)

logger.info("-" * 50)
logger.info(f"Date - : {current_date}")
# Print post count, file size, and post count per day
logger.info(f"Total post count: {post_data['POST_COUNT']}")
logger.info(f"File size (in bytes): {post_data['FILE_SIZE']}")
logger.info(f"Post count per day: {post_data['post_count_per_day']}")

# Create a stream listener object
listener = MyStreamListener()

# Start streaming for new toots
mastodon.stream_public(listener)

