import logging
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)
        self.username_input = page.get_by_placeholder("请输入登录的手机号")
        self.password_input = page.get_by_placeholder("请输入登录密码")
        self.confirm_button = page.locator("span[class='el-checkbox__input']")
        self.login_button = page.get_by_role("button", name="立即登录")

    def navigate(self, url: str):
        self.logger.info(f"导航到页面: {url}")
        self.page.goto(url)
        self.logger.debug("页面导航完成")

    def input_username(self, username: str):
        self.logger.info(f"正在输入用户名: {username}")
        self.username_input.fill(username)
        self.logger.debug("用户名输入完成")

    def input_password(self, password: str):
        self.logger.info("正在输入密码")
        self.password_input.fill(password)
        self.logger.debug("密码输入完成")

    def click_confirm_button(self):
        self.logger.info("点击确认按钮")
        self.confirm_button.click()
        self.logger.debug("确认按钮点击完成")

    def click_login_button(self):
        self.logger.info("点击登录按钮")
        self.login_button.click()
        self.logger.debug("登录按钮点击完成")

    def assert_login_success(self):
        # 等待页面URL变化
        self.page.wait_for_url(lambda url: "dashboard" in url, timeout=5000)  # 10秒超时
        current_url = self.page.url
        self.logger.info(f"验证登录成功 当前URL: {current_url}")
        if "dashboard" not in current_url:
            self.logger.error(f"登录失败，当前URL: {current_url}")
            assert False, "登录失败"
        self.logger.info("登录验证成功")
    
    def assert_login_fail(self, error_message: str):
        self.logger.info(f"验证登录失败，错误信息: {error_message}")
        # 等待错误提示出现
        error_element = self.page.get_by_text(error_message)
        error_element.wait_for(state="visible", timeout=3000)  # 5秒超时
