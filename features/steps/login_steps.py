from pytest_bdd import given, when, then, parsers
from pytest_bdd.parsers import string

from pages.login_page import LoginPage
from pytest import fixture

@fixture(scope="function")
def login_page(page):
    login_page = LoginPage(page)
    yield login_page

@given('我在登录页面')
def navigate_to_login_page(login_page):
    login_page.navigate("https://testcenter.qdhdkj.com/login")

@when(parsers.parse('我输入用户名 "{username}"'))
def input_username(login_page,username):
    login_page.input_username(username)

@when(parsers.parse('我输入密码 "{password}"'))
def input_password(login_page,password):
    login_page.input_password(password)

@when('点击登录按钮')
def click_login_button(login_page):
    login_page.click_confirm_button()
    login_page.click_login_button()

@then('我应该看到 Dashboard 页面')
def assert_login_success(login_page):
    login_page.assert_login_success()



