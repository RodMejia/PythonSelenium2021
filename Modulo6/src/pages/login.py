from selenium.webdriver.remote.webdriver import WebDriver
from Modulo6.src.elements.base_page_element import BasePageElement
from Modulo6.src.locators.login import LoginPageLoc
from Modulo6.src.pages.base_page import BasePage
from Modulo6.src.pages.inventory import InventoryPage


_URL = 'https://www.saucedemo.com/'


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.__user = BasePageElement(LoginPageLoc.USER, wait=self._wait)
        self.__password = BasePageElement(LoginPageLoc.PASSWORD, wait=self._wait)
        self.__login = BasePageElement(LoginPageLoc.LOGIN, wait=self._wait)
        self.__error_msg = BasePageElement(LoginPageLoc.ERROR_MSG, wait=self._wait)

    def login(self, user, password):
        self.__user.write(user)
        self.__password.write(password)
        self.__login.click()
        return InventoryPage(self._driver, self._timeout)

    def get_error_message(self) -> str:
        #return: Error message
        return self.__error_msg.get_text()