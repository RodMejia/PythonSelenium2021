from typing import List
from selenium.webdriver.remote.webelement import WebElement

from Common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = get_driver('chrome')
driver.implicitly_wait(10)

driver.get('https://www.amazon.com')

elements = driver.find_elements_by_xpath("//a")

for element in elements:
    print(element.text)

hijos_head = driver.find_elements_by_xpath('//head/*')
for element in hijos_head:
    print(f"{element.text} - {element.get_attribute('href')}")

driver.quit()