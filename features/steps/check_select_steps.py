from pytest_bdd import given, when, then, parsers
from pytest import fixture
from pages.tiktok_page import TikTokPage

@fixture(scope="function")
def check_select_page(page):
    check_select_page = TikTokPage(page)
    yield check_select_page

@given('我已登录系统')
def already_logged_in(check_select_page):
    check_select_page.navigate_to_home()

@when(parsers.parse('我在筛选栏输入 "{condition}"'))
def input_filter_condition(check_select_page, condition):
    check_select_page.input_filter_condition(condition)

@then(parsers.parse('我应该看到 "{expected_result}"'))
def assert_filter_result(check_select_page, expected_result):
    check_select_page.assert_filter_result(expected_result)