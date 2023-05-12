import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function")
def browser_start():
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.config.base_url = 'https://github.com'
    yield
    browser.quit()