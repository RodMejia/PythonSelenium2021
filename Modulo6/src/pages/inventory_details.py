from selenium.webdriver.remote.webdriver import WebDriver
from Modulo6.src.elements.menu import Menu
from Modulo6.src.elements.base_page_element import BasePageElement
from Modulo6.src.elements.header import Header
from Modulo6.src.locators.inventory_details import InventoryDetailsLoc
from Modulo6.src.mixin.InventoryItemMixin import InventoryItemMixin
from Modulo6.src.pages.base_page import BasePage

_URL = 'https://www.saucedemo.com/inventory-item.html?id={0}'

class InventoryDetailsPage(BasePage, InventoryItemMixin):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self._title = BasePageElement(InventoryDetailsLoc.TITLE, wait=self._wait)
        self._description = BasePageElement(InventoryDetailsLoc.DESCRIPTION, wait=self._wait)
        self._price = BasePageElement(InventoryDetailsLoc.PRICE, wait=self._wait)
        self._inv_btn = BasePageElement(InventoryDetailsLoc.BTN, wait=self._wait)
        self._back_btn = BasePageElement(InventoryDetailsLoc.BACK_BTN, wait=self._wait)
        self.header = Header(self._wait)
        self.menu = Menu(self._wait)

    def back(self):
        self._back_btn.click()