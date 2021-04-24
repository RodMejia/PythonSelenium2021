from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Modulo6.src.elements.overview_item import OverviewItem


class OverviewItems:

    def __init__(self, loc: tuple, wait: WebDriverWait = None):
        self._wait = wait
        self._loc = loc
        self.__elements = []


    def reload(self):
        """Force reload of inventory items."""
        self.__elements.clear()
        elements = self._wait.until(EC.visibility_of_all_elements_located(self._loc))
        for element in elements:
            inv_item = OverviewItem(self._wait, element)
            self.__elements.append(inv_item)

    def __getitem__(self, key):
        if not self.__elements:
            self.reload()
        return self.__elements[key]

    def __iter__(self):
        self.reload()
        return iter(self.__elements)

    def __len__(self):
        return len(self.__elements)