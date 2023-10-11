import pytest
import json
from selenium import webdriver

@pytest.fixture(scope='session')
def config():
    with open('settings.json', 'r') as f:
        settings = json.loads(f.read())
    return settings


@pytest.fixture(scope='session')
def driver(config):
    if config['browser'] == 'Chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
