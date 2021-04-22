
from Modulo6.src.elements.base_page_element import BasePageElement
from selenium.webdriver.remote.webelement import WebElement
from Modulo6.src.locators.cartitems import CartItemLoc
from selenium.webdriver.support.wait import WebDriverWait
from Modulo6.src.mixin.CartItemMixin import CartItemMixin
from Modulo6.src.pages.inventory_details import InventoryDetailsPage


class CartItem(CartItemMixin):
    """Sauce lab login."""

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._wait = wait
        self._title = BasePageElement(CartItemLoc.TITLE, wait=wait, root=root)
        self._description = BasePageElement(CartItemLoc.DESCRIPTION, wait=wait, root=root)
        self._price = BasePageElement(CartItemLoc.PRICE, wait=wait, root=root)
        self._remove = BasePageElement(CartItemLoc.REM_BTN, wait=wait, root=root)


    def open_details(self):
        """Open product details"""
        self._title.click()
        return InventoryDetailsPage(self._wait._driver, self._wait._timeout)


