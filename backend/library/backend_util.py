"""
Purpose:
    This script used to read the data from mastodon.config file
    and pass these data to other modules in backend.
Inputs:
    - No inputs to this file
Outputs:
    The mastodon configurations will be passed.
Author: Pasan Kamburugamuwa
"""

import configparser
import logging
import traceback
import argparse
import os
import sys
import json
from psycopg2 import pool
from contextlib import contextmanager

def get_mastodon_conf():
    """
    Get the mastodon configuration file.
    """
    try:
        config_file_path = "./config/mastodon.config"
        config_parser = configparser.ConfigParser()
        config_parser.read(config_file_path)
        return config_parser
    except FileNotFoundError as fnf_error:
        traceback.print_tb(fnf_error.__traceback__)
        raise Exception('Unable to find the mastodon config file')

def get_flask_host():
    """
    Get the flask host.
    """
    try:
        config = get_mastodon_conf()
        flask_host = config["DEFAULT"]["FlaskHost"]
        return flask_host
    except Exception as exc:
        traceback.print_tb(exc.__traceback__)
        raise Exception('Unable to find the mastodon flask host')

def get_flask_port():
    """
    Get the flask port.
    """
    try:
        config = get_mastodon_conf()
        flask_port = config["DEFAULT"]["FlaskPort"]
        return flask_port
    except Exception as exc:
        traceback.print_tb(exc.__traceback__)
        raise Exception('Unable to find the mastodon flask port')

def get_flask_debug_mode():
    """
    Get the flask debug mode.
    """
    try:
        config = get_mastodon_conf()
        flask_debug_mode = config["DEFAULT"]["DebugMode"]
        return flask_debug_mode
    except Exception as exc:
        traceback.print_tb(exc.__traceback__)
        raise Exception('Unable to find the mastodon debug mode')

def get_instances_social_api_key():
    """
    Get the Mastodon API key.
    :return: Mastodon API key.

    Info - The API key is from the https://instances.social/ and it is used to get instances.
    """
    try:
        api_key_file_path = "./config/keys.json"
        if not os.path.exists(api_key_file_path):
            raise Exception("API key file not found")

        with open(api_key_file_path) as file:
            credentials = json.load(file)

        #Get the instance social API key from the json file.
        mastodon_api_key = credentials.get("InstancesSocialAPIKey")
        if mastodon_api_key:
            return mastodon_api_key
        else:
            raise Exception("Mastodon API key not found in the JSON file")
    except Exception as exc:
        traceback.print_tb(exc.__traceback__)
        raise Exception("Unable to find the Mastodon API key")
def get_mastodon_social_server_access_token():
    """
    Get the Mastodon Social Server Access token
    :return: Mastodon Social Server Access Token.

    Info - The access token is from the https://mastodon.social/settings/applications/ and it is used to get the posts
    Drawback : This token is used to get only the posts for the specific server. Not all the server data.
    """
    try:
        mastodon_server_access_file_path = "./config/keys.json"
        if not os.path.exists(mastodon_server_access_file_path):
            raise Exception("Mastodon server access file not found")

        with open(mastodon_server_access_file_path) as file:
            credentials = json.load(file)

        #Get the instance social API key from the json file.
        mastodon_social_access_token = credentials.get("mastodonOneServerAPIKey")
        if mastodon_social_access_token:
            return mastodon_social_access_token
        else:
            raise Exception("Mastodon social access key is not found in the JSON file")
    except Exception as exc:
        traceback.print_tb(exc.__traceback__)
        raise Exception("Unable to find the Mastodon social access key!")


def get_database_host():
    """
    Get the database host.
    """
    try:
        config = get_mastodon_conf()
        database_host = config["POSTGRESQL_DATABASE"]["database-host"]
        return database_host
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find the postgresql database host')

def get_database_port():
    """
    Get the database port.
    """
    try:
        config = get_mastodon_conf()
        database_port = config["POSTGRESQL_DATABASE"]["database-port"]
        return database_port
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find the postgresql database port')

def get_database_name():
    """
    Get the database name.
    """
    try:
        config = get_mastodon_conf()
        database_name = config["POSTGRESQL_DATABASE"]["database-name"]
        return database_name
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find the postgresql database name')

def get_database_username():
    """
    Get the database username.
    """
    try:
        config = get_mastodon_conf()
        database_username = config["POSTGRESQL_DATABASE"]["database-username"]
        return database_username
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find the postgresql database username')

def get_database_password():
    """
    Get the database password.
    """
    try:
        config = get_mastodon_conf()
        database_password = config["POSTGRESQL_DATABASE"]["database-password"]
        return database_password
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        raise Exception('Unable to find the postgresql database password')

db = None

# Create the database connection.
try:
    db = pool.SimpleConnectionPool(1,
                                10,
                                host=get_database_host(),
                                database=get_database_name(),
                                user=get_database_username(),
                                password=get_database_password(),
                                port=get_database_port())
except Exception as e:
    print("Error initializing connection pool:", str(e))

@contextmanager
def get_db_connection():
    """
    Get the database connection.
    """
    if db is None:
        # Handle the case where the connection pool is not initialized.
        raise RuntimeError("Connection pool is not initialized.")

    con = db.getconn()
    try:
        yield con
    finally:
        db.putconn(con)

@contextmanager
def get_db_cursor():
    """
    Get the db cursor.
    """
    with get_db_connection() as connection:
        cursor = connection.cursor()
        try:
            yield cursor
            connection.commit()
        finally:
            cursor.close()

def get_logger(log_dir, log_fname, script_name=None, also_print=False):
    """
    Create logger for the project.
    """
    # Create log_dir if it doesn't exist already
    try:
        os.makedirs(f"{log_dir}")
    except:
        pass

    # Create logger and set level
    logger = logging.getLogger(script_name)
    logger.setLevel(level=logging.INFO)

    # Configure file handler
    formatter = logging.Formatter(
        fmt="%(asctime)s-%(name)s-%(levelname)s - %(message)s",
        datefmt="%Y-%m-%d_%H:%M:%S",
    )
    full_log_path = os.path.join(log_dir, log_fname)
    fh = logging.FileHandler(f"{full_log_path}")
    fh.setFormatter(formatter)
    fh.setLevel(level=logging.INFO)
    # Add handlers to logger
    logger.addHandler(fh)

    # If also_print is true, the logger will also print the output to the
    # console in addition to sending it to the log file
    if also_print:
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        ch.setLevel(level=logging.INFO)
        logger.addHandler(ch)
    return logger
