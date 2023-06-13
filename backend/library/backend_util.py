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

logger = logging.getLogger(__name__)

def get_mastodon_conf():
    """
    Get the mastodon configuration file.
    """
    try:
        config_file_path = "./config/mastodon.config"
        logger.info('FibIndex conf path : %s', config_file_path)
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
        logger.error("Error in finding the mastodon flask host")
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
        logger.error("Error in finding the mastodon flask port")
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
        logger.error("Error in finding the mastodon debug mode")
        raise Exception('Unable to find the mastodon debug mode')


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
