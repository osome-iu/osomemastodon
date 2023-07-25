"""
Purpose:
    This script used to get the mastodon_streamer api and data. post data.
Inputs:
    - functions
        - get_file_name (get the file name)
        - on_update(call the get data function)
        - print_posts_and_file_size(print post and file size)

Outputs:
    - JSON object
Authors: Pasan Kamburugamuwa
"""

import json
import os
import datetime
import time
from mastodon import Mastodon, StreamListener
from library import backend_util

# Specify the directory path where the files will be stored
#DATA_DERIVED_DIR = "/home/pkamburu/mastodon/data_derived"
DATA_DERIVED_DIR = "/home/data/apps/mastodon/data_derived"
LOG_DIR = "/home/data/apps/mastodon/log"

# Create a logger
LOG_FNAME = "mastodon_logging.log"
script_name = os.path.basename(__file__)
logger = backend_util.get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)


# Define a custom stream listener
class MastodonStreamListener(StreamListener):
    def __init__(self, instance_name, stream_method):
        super().__init__()

        self.instance_name = instance_name
        self.stream_method = stream_method

        self.current_hour_posts = 0
        self.posts_count_per_day = 0

        # Get the current date
        self.current_date = datetime.datetime.now().date()
        # Get the current hour
        self.current_hour = datetime.datetime.now().hour
        self.file_name = self.get_file_name()

    def get_file_name(self):
        # Get the current month and date for the filename
        current_month = datetime.datetime.now().strftime("%Y-%m")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Create the directory if it doesn't exist
        os.makedirs(os.path.join(DATA_DERIVED_DIR, current_month), exist_ok=True)
        return os.path.join(DATA_DERIVED_DIR, current_month, f"{self.instance_name}_{self.stream_method}_{current_date}.json")

    def on_update(self, status):
        """
        Increment the post count for each received toot
        Parameters
        -----------
        None
        Returns
        -----------
        .gz file create and remove the mastodon_{current_date}.json file.
        """
        # Increment the post count for each received toot
        self.posts_count_per_day += 1
        self.current_hour_posts += 1

        #In this function is used to check if there is a new date started.
        now = datetime.datetime.now()
        if now.date() != self.current_date:
            self.end_of_date()

        # Check if an hour has passed, print the result and reset the counter
        current_hour = datetime.datetime.now().hour
        if current_hour != self.current_hour:
            self.log_posts_and_file_size()
            self.current_hour_posts = 1
            self.current_hour = current_hour


        # Check if the status is a reply
        is_reply = 'in_reply_to_id' in status and status['in_reply_to_id'] is not None

        # Get the replied post URL
        replied_post_url = None
        if is_reply:
            replied_post_id = status['in_reply_to_id']
            replied_post_url = f"{status['account']['url']}status/{replied_post_id}"

        # Write toot info to JSON file
        toot_info = {
            'content': status['content'],
            'username': status['account']['username'],
            'status_id': status['id'],
            'created_at': status['created_at'],
            'visibility': status['visibility'],
            'post_url': status['url'],
            'is_reply': is_reply,
            'replied_post_url': replied_post_url  # Add the replied_post_url field
        }

        # Create directories for the current month and date if they don't exist
        os.makedirs(os.path.dirname(self.file_name), exist_ok=True)

        with open(self.file_name, 'a') as file:
            json.dump(toot_info, file, default=str)
            file.write('\n')

    def log_posts_and_file_size(self):
        """
        This function is used to print the post size and file size for each hour.
        Parameters
        -----------
        None
        Returns
        -----------
        .gz file create and remove the mastodon_{current_date}.json file.
        """
        current_hour = datetime.datetime.now().hour
        previous_hour = (current_hour - 1) % 24

        # Get file size in bytes
        file_size = os.path.getsize(self.file_name)

        # Print the result
        logger.info(f"Hour {previous_hour}: {self.current_hour_posts} posts, "
              f"File size: {file_size} bytes")


    def end_of_day(self):
        """
        This function is used to store the json file in a .gz file and remove the original json file.
        Parameters
        -----------
        None
        Returns
        -----------
        .gz file create and remove the mastodon_{current_date}.json file.
        """
        # Close the current JSON file if it's open
        if self.current_file:
            self.current_file.close()

        # Gzip the previous day's JSON file
        if os.path.isfile(self.file_name):
            with open(self.file_name, 'rb') as file:
                with gzip.open(self.file_name + '.gz', 'wb') as gzip_file:
                    gzip_file.writelines(file)

            # Remove the original JSON file
            os.remove(self.file_name)

        logger.info("-" * 50)
        logger.info(f"End of the Day: {__file__}")

        logger.info(f"Date {self.current_date}: {self.posts_count_per_day} posts, "
              f"File size: {file_size} bytes")
        logger.info("-" * 50)


        # Reset counters and file info for the new day
        self.current_date = datetime.datetime.now().date()
        self.current_hour = datetime.datetime.now().hour
        self.current_hour_posts = 0

        self.file_name = f"{self.instance_name}_{self.stream_method}_{self.current_date}.json"
        self.current_file = None


def stream_public_data(instance_info):
    # Create a Mastodon client
    mastodon_stream = Mastodon(
        access_token=instance_info['access_token'],
        api_base_url=instance_info['instance_name']
    )

    # Use the access token for user streaming
    mastodon_stream.access_token = instance_info['access_token']

    stream_listener = MastodonStreamListener(instance_info['instance_name'], instance_info['stream_method'])
    mastodon_stream.stream_public(stream_listener)


def stream_local_data(instance_info):
    # Create a Mastodon client
    mastodon_stream = Mastodon(
        access_token=instance_info['access_token'],
        api_base_url=instance_info['instance_name']
    )

    # Use the access token for user streaming
    mastodon_stream.access_token = instance_info['access_token']

    stream_listener = MastodonStreamListener(instance_info['instance_name'], instance_info['stream_method'])
    mastodon_stream.stream_local(stream_listener)