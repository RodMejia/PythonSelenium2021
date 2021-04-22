from selenium.webdriver.remote.webdriver import WebDriver
from Modulo6.src.elements.base_page_element import BasePageElement
from Modulo6.src.locators.google import GoogleLocators
from Modulo6.src.pages.base_page import BasePage

_URL = 'https://www.google.com/'


class Google(BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.__search_textbox = BasePageELement(GoogleLocators.SEARCH_TEXT_BOX, wait=self._wait)
        self.__search_btn = BasePageELement(GoogleLocators.SEARCH_BTN, wait=self._wait)
        self.__feeling_lucky_btn = BasePageELement(GoogleLocators.FEELING_LUCKY_BTN, wait=self._wait)

    def search(self, value):
        self.__search_textbox.write(value)
        self.__search_btn.click()

    def feeling_lucky(self, value):
        self.__search_textbox.write(value)
        self.__feeling_lucky_btn.click()
