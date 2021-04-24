from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from Modulo6.src.elements.base_page_element import BasePageElement
from Modulo6.src.locators.overview_items import OverviewItemsLoc
from Modulo6.src.mixin.OverviewItemMixin import OverviewItemMixin


class OverviewItem(OverviewItemMixin):

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._wait = wait
        self._title = BasePageElement(OverviewItemsLoc.TITLE, wait=wait, root=root)
        self._description = BasePageElement(OverviewItemsLoc.DESCRIPTION, wait=wait, root=root)
        self._price = BasePageElement(OverviewItemsLoc.PRICE, wait=wait, root=root)


