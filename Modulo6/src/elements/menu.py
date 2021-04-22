from selenium.webdriver.support.wait import WebDriverWait
from Modulo6.src.elements.base_page_element import BasePageElement
from Modulo6.src.locators.menu import MenuLoc


class Menu:

    def __init__(self, wait: WebDriverWait):
        self._wait = wait
        self._all_items = BasePageElement(MenuLoc.ALL_ITEMS, wait=wait)
        self._about = BasePageElement(MenuLoc.ABOUT, wait=wait)
        self._logout = BasePageElement(MenuLoc.LOGOUT, wait=wait)
        self._burger_btn = BasePageElement(MenuLoc.BURGER_BTN, wait=wait)

    def logout(self):
        self._logout.click()

    def open_menu(self):
        """Open menu"""
        self._burger_btn.click()

    def back_to_inventory(self):
        self._all_items.click()

