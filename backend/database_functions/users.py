"""
Purpose:
    Add the users to the user table.

Inputs:
    None

Outputs:
    None

Authors: Pasan Kamburugamuwa
"""

from flask import Flask
from library import backend_util

app = Flask(__name__)

def add_users(id, instance, username, acct, display_name, locked, bot, created_at, avatar, followers_count, following_count, statuses_count, last_status_at):
    """
    Add data to the users table.

    Parameters
    -----------
    - id (primary key - str): this is an unique key for getting from the mastodon search API
    - instance - name of the instance the user belongs to.
    - username : username of the mastodon user(ex- jrashf)
    - acct - account name(this will include both the username and the instance) ex-jrashf@mastodonapp.uk
    - locked - Is the account locked or not. (visibility)
    - bot - is it a bot(True or False)
    - discoverable - discoverable or not (True or False)
    - created_at - Account created date
    - avatar - Avatar Image
    - followers_count - No of followers have
    - following_count - No of following users the user has
    - statuses_count - No of posts
    - last_status_at - Last post created
    Returns
    -----------
    result (dict): {'id': mastodon_user_id}
    """
    with backend_util.get_db_cursor() as cur:
        try:
            add_user = (
                "INSERT INTO users"
                "(id, instance, username, acct, display_name, locked, bot, created_at, avatar, followers_count, following_count, statuses_count, last_status_at) "
                "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
                "RETURNING id"
            )
            cur.execute(
                add_user,
                (id, instance, username, acct, display_name, locked, bot, created_at, avatar, followers_count, following_count, statuses_count, last_status_at),
            )
            if cur.rowcount > 0:
                mastodon_user_id = cur.fetchone()[0]
                result = {"id": mastodon_user_id}
                print(result)
            return result
        except Exception as ex:
            raise Exception(ex)

def check_user_already_exist(id):
    """
    Check the user is already exists or not.

    Parameters
    -----------
    - id (primary key - str): this is an unique key for getting from the mastodon search API
    Returns
    -----------
    result : True or False
    """
    with backend_util.get_db_cursor() as cur:
        try:
            get_user = "select * from users where id = %s"
            cur.execute(get_user, (id,))
            if cur.rowcount > 0:
                return True
            return False
        except Exception as ex:
            raise Exception(ex)

def update_existing_user(instance, username, acct, display_name, locked, bot, created_at, avatar, followers_count, following_count, statuses_count, last_status_at, id):
    """
    Update the existing user with the new request values

    Parameters
    -----------
    - id (primary key - str): this is an unique key for getting from the mastodon search API
    - instance - name of the instance the user belongs to.
    - username : username of the mastodon user(ex- jrashf)
    - acct - account name(this will include both the username and the instance) ex-jrashf@mastodonapp.uk
    - locked - Is the account locked or not. (visibility)
    - bot - is it a bot(True or False)
    - discoverable - discoverable or not (True or False)
    - created_at - Account created date
    - avatar - Avatar Image
    - followers_count - No of followers have
    - following_count - No of following users the user has
    - statuses_count - No of posts
    - last_status_at - Last post created
    Returns
    -----------
    result (dict): {'id': mastodon_user_id}
    """
    with backend_util.get_db_cursor() as cur:
        try:
            result = {}
            update_user = (
                "UPDATE users "
                "SET instance = %s, "
                "username = %s, "
                "acct = %s, "
                "display_name = %s, "
                "locked = %s, "
                "bot = %s, "
                "created_at = %s, "
                "avatar = %s, "
                "followers_count = %s, "
                "following_count = %s, "
                "statuses_count = %s, "
                "last_status_at = %s "
                "WHERE id = %s "
            )
            cur.execute(
                update_user,
                (instance, username, acct, display_name, locked, bot, created_at, avatar, followers_count, following_count, statuses_count, last_status_at, id),
            )
            return result
        except Exception as ex:
            raise Exception(ex)

def get_user_data(user_id):
    """
    Get the user data for the selected user_id

    Parameters
    -----------
    - id (primary key - str): this is the unique id which is used to get the user.
    Returns
    -----------
    result : user object
    """
    with backend_util.get_db_cursor() as cur:
        try:
            get_user = "select * from users where id = %s"
            cur.execute(get_user, (user_id,))
            if cur.rowcount>0:
                return cur.fetchone()
            else:
                return {}
        except Exception as ex:
            raise Exception(ex)