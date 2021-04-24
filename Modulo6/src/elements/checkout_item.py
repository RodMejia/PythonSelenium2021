from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from Modulo6.src.elements.base_page_element import BasePageElement
from Modulo6.src.locators.checkout import ChkOutPageLoc


class CheckOutElements:

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._wait = wait
        self._title = BasePageElement(ChkOutPageLoc.TITLE, wait=wait, root=root)
        self._first_name = BasePageElement(ChkOutPageLoc.FIRST_NAME, wait=wait, root=root)
        self._last_name = BasePageElement(ChkOutPageLoc.LAST_NAME, wait=wait, root=root)
        self._zip_code = BasePageElement(ChkOutPageLoc.ZIP_CODE, wait=wait, root=root)
        self._cancel_btn = BasePageElement(ChkOutPageLoc.CANCEL, wait=wait, root=root)
        self._continue_btn = BasePageElement(ChkOutPageLoc.CONTINUE, wait=wait, root=root)


    def open_overview(self):
        self._continue_btn.click()