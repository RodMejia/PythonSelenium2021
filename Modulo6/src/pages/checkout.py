from selenium.webdriver.remote.webdriver import WebDriver
from Modulo6.src.elements.base_page_element import BasePageElement
from Modulo6.src.locators.checkout import ChkOutPageLoc
from Modulo6.src.pages.base_page import BasePage
from Modulo6.src.pages.cart import CartPage

_URL = 'https://www.saucedemo.com/checkout-step-one.html'

class CheckFormPage(BasePage):


    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self._title = BasePageElement(ChkOutPageLoc.TITLE, wait=self._wait)
        self.__first_name = BasePageElement(ChkOutPageLoc.FIRST_NAME, wait=self._wait)
        self.__last_name = BasePageElement(ChkOutPageLoc.LAST_NAME, wait=self._wait)
        self.__zip_code = BasePageElement(ChkOutPageLoc.ZIP_CODE, wait=self._wait)
        self._cancel_btn = BasePageElement(ChkOutPageLoc.CANCEL, wait=self._wait)
        self._continue_btn = BasePageElement(ChkOutPageLoc.CONTINUE, wait=self._wait)
        self.__error_msg = BasePageElement(ChkOutPageLoc.ERROR_MSG, wait=self._wait)

    def get_label(self) -> str:
        """Get page label."""
        return self._title.get_text()

    def login(self, f_name, l_name, z_code):
        self.__first_name.write(f_name)
        self.__last_name.write(l_name)
        self.__zip_code.write(z_code)

    def cancel(self):
        self._cancel_btn.click()
        return CartPage(self._wait._driver, self._wait._timeout)

    def get_error_message(self) -> str:
        #return: Error message
        return self.__error_msg.get_text()

    def cont_btn(self):
        self._continue_btn.click()
