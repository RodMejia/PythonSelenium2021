from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Common.webdriver_factory import get_driver


def select_dropdown(wait: WebDriverWait, option: str):
    locator = (By.XPATH, "//select[contains(@class,'p-dropdown__standings')]")
    element = wait.until(EC.element_to_be_clickable(locator))
    dropdown = Select(element)
    dropdown.select_by_value(option)


def select_std(wait: WebDriverWait):
    locator = (By.XPATH, "//button[@data-value ='standard']")
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()


def select_advanced(wait: WebDriverWait):
    locator = (By.XPATH, "//button[@data-value ='advanced']")
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

if __name__ == '__main__':
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.mlb.com/es/standings')

    select_dropdown(wait, 'league')

    select_std(wait)

    select_advanced(wait)

    driver.quit()


