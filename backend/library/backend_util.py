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
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file_path = os.path.join(project_root, "mastodon.config")

def get_mastodon_conf():
    """
    Get the mastodon configuration file.
    """
    try:
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

def get_instances_file():
    """
    Get the top Mastodon instances
    """
    try:
        config = get_mastodon_conf()
        instances_file = config["DEFAULT"]["InstancesFile"]
        return instances_file
    except Exception as exc:
        traceback.print_tb(exc.__traceback__)
        raise Exception('Unable to find the instance file')

def get_logger(script_name=None, also_print=True):
    """
    Create logger for the project.
    """
    config = get_mastodon_conf()
    logger_file = config["DEFAULT"]["LoggerFile"]

    # Create logger and set level
    logger = logging.getLogger(script_name)
    logger.setLevel(level=logging.INFO)

    # Create formatter
    formatter = logging.Formatter(fmt="%(asctime)s-%(name)s-%(levelname)s - %(message)s", datefmt="%Y-%m-%d_%H:%M:%S")

    fh = logging.FileHandler(f"{logger_file}")
    fh.setFormatter(formatter)
    fh.setLevel(level=logging.INFO)

    # Add handlers to logger
    logger.addHandler(fh)

    # If also_print is true, this will print to the console.
    if also_print:
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        ch.setLevel(level=logging.INFO)
        logger.addHandler(ch)
    return logger
