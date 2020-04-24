from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page.basepage import BasePage


class MinePage(BasePage):

    _account_button = BasePage.by_id("login_account")
    _password_button = BasePage.by_id("button_next")
    _login_button = BasePage.by_id("button_next")
    _message_login_fail = BasePage.by_id("md_content")

    def __login_by_phone(self, phone, captch):
        self.driver.tap([(16, 166), (464, 194)])
        self.find(self._account_button).send_keys(phone)
        self.find(self._password_button).send_keys(captch)
        self.find(self._login_button).click()

    def login_fail(self, phone, captch):
        self.__login(phone, captch)
        return self._message_login_fail.text

    def login_successful(self, phone, captch):
        self.__login(phone, captch)
        return self
