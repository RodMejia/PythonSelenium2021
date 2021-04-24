from Modulo6.src.elements.base_page_element import BasePageElement
from Modulo6.src.elements.overview_items import OverviewItems
from Modulo6.src.locators.overview import OverPageLoc
from Modulo6.src.locators.overview_items import OverviewItemsLoc
from Modulo6.src.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from Modulo6.src.elements.header import Header
from Modulo6.src.elements.menu import Menu


_URL = 'https://www.saucedemo.com/checkout-step-two.html'

class Overview(BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.header = Header(self._wait)
        self.menu = Menu(self._wait)
        self.products = OverviewItems(OverPageLoc.ITEMS, self._wait)
        self.__label = BasePageElement(OverPageLoc.TITLE, self._wait)
        self.__sub_label = BasePageElement(OverPageLoc.SUB_TOTAL, self._wait)
        self.__tax_label = BasePageElement(OverPageLoc.TAX, self._wait)
        self.__total_label = BasePageElement(OverPageLoc.TOTAL, self._wait)
        self.__cancel_btn = BasePageElement(OverPageLoc.BACK, self._wait)
        self.__finish_btn = BasePageElement(OverPageLoc.FINISH, self._wait)

    def get_page_label(self):
        return self.__label.get_text()

    def get_sub_label(self):
        return self.__sub_label.get_text()

    def get_tax(self):
        return self.__tax_label.get_text()

    def get_total(self):
        return self.__total_label.get_text()

    def go_back_to_catalog(self):
        self.__cancel_btn.click()

    def finish(self):
        self.__finish_btn.click()