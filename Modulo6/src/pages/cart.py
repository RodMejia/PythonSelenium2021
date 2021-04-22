
from selenium.webdriver.remote.webdriver import WebDriver
from Modulo6.src.elements.items_cart import CartItems
from Modulo6.src.elements.header import Header
from Modulo6.src.elements.menu import Menu
from Modulo6.src.locators.cart import CartPageLoc
from Modulo6.src.pages.base_page import BasePage
from Modulo6.src.elements.base_page_element import BasePageElement
from Modulo6.src.pages.inventory import InventoryPage

_URL = 'https://www.saucedemo.com/cart.html'


class CartPage(BasePage):
    """Sauce lab login."""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.header = Header(self._wait)
        self.menu = Menu(self._wait)
        self.products = CartItems(CartPageLoc.ITEMS, self._wait)
        self.__label = BasePageElement(CartPageLoc.TITLE, self._wait)
        self._back = BasePageElement(CartPageLoc.BACK, self._wait)
        self._checkout = BasePageElement(CartPageLoc.CHK_BTN, self._wait)


    def get_label(self) -> str:
        """Get page label."""
        return self.__label.get_text()

    def go_back(self):
        self._back.click()
        return InventoryPage(self._wait._driver, self._wait._timeout)

    def check_out(self):
        self._checkout.click()