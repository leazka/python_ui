"""
This module contains fixtures for web UI tests.
"""

import json
import pytest

from selenium.webdriver import Chrome

CONFIG_PATH = 'config.json'
DEFAULT_WAIT_TIME = 10


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def config_driver_path(config):
    # Return the driver path from the config data
    if 'driver_path' not in config:
        raise Exception('The config file does not contain path to the webdriver"')
    return config['driver_path']


@pytest.fixture
def browser(config_driver_path):
    # Initialize WebDriver
    driver = Chrome(config_driver_path)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()
