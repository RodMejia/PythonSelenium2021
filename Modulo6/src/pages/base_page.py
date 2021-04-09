import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    __MAX_TIMEOUT = 6000

    __MIN_TIMEOUT = 0

    def __init__(self, driver: WebDriver, url: str = None, timeout: int = 10):
        self._driver = driver
        self._url = url
        self._wait = WebDriverWait(self._driver, timeout)
        self.timeout = timeout

    def open(self):
        self._driver.get(self._url)

    def close(self):
        self._driver.close()

    def wait_until_loaded(self):
        logging.info(f'Wait until page {self._url} is loaded')
        return True

    @property
    def timeout(self, value):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        if value < BasePage.__MIN_TIMEOUT or value > BasePage.__MAX_TIMEOUT:
            raise ValueError(f'Invalid value for timeout: {value}')
        self._timeout = value
        if self._wait._timeout != value:
            self._wait._timeout = value