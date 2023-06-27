"""
Purpose:
    Add the posts to the database.

Inputs:
    None

Outputs:
    None

Authors: Pasan Kamburugamuwa
"""

from flask import Flask
from library import backend_util

app = Flask(__name__)

def add_posts(id, instance,user_id,username,is_bot, post, url):
    """
    Add data to the posts table.

    Parameters
    -----------
    - id (str): a social media users unique identifying post(status_id)
    - instance (str): instance id
    - user_id (int/float): the user_id
    - username (str): username of the post belong to user
    - username (str): the username of `user_id`
    - platform (str): the name of the platform (should be "twitter" or "facebook")

    Returns
    -----------
    result (dict): {'id': statuses_id}
    """
    with backend_util.get_db_cursor() as cur:
        try:
            add_posts = (
                "INSERT INTO posts "
                "(id, instance, user_id, username, is_bot, post, url) "
                "values (%s, %s, %s, %s, %s, %s, %s) "
                "RETURNING user_id"
            )
            cur.execute(
                add_posts,
                (id, instance, user_id, username, is_bot, post, url),
            )
            if cur.rowcount > 0:
                post_id = cur.fetchone()[0]
                result = {"id": post_id}
            return result
        except Exception as ex:
            raise Exception(ex)


