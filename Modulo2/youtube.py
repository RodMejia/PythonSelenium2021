from typing import List
from selenium.webdriver.remote.webelement import WebElement

from Common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = get_driver('chrome')
wait = WebDriverWait(driver,5)

driver.get('https://www.youtube.com')

locator = (By.ID, 'search')
search_textbox = wait.until(EC.visibility_of_element_located(locator))
search_textbox.send_keys('Selenium')

button_search = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
button_search.click()

title_selenium = driver.find_elements_by_tag_name('')
print(title_selenium[0:5])

driver.quit()

