import pytest
import logging
from playwright.sync_api import sync_playwright

log = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="function")
def browser_type(playwright):
    return playwright.chromium

@pytest.fixture(scope="function")
def browser(browser_type):
    browser = browser_type.launch(headless=False)
    log.info("启动浏览器")
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()
    log.info("关闭浏览器")

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
    log.info("页面关闭")