"""Saucelab login example"""
from selenium.webdriver.remote.webelement import WebElement

from Common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(wait: WebDriverWait, user: str, secret: str):
    """login to sauce lab

    :param wait: instance of webdriverwait
    :param user: valid user
    :param secret: valid password
    :return:
    """
    user_locator = (By.ID, 'user-name')
    user_element = wait.until(EC.element_to_be_clickable(user_locator))
    user_element.clear()
    user_element.send_keys(user)

    password_locator = (By.ID, 'password')
    password_element = wait.until(EC.element_to_be_clickable(password_locator))
    password_element.clear()
    password_element.send_keys(user)

    login_locator = (By.ID, 'login-button')
    login_element = wait.until(EC.element_to_be_clickable(login_locator))
    login_element.click()


def get_catalog_info(wait: WebDriverWait) -> list:
    """get catalog information"""
    result = []
    products_locator = (By.CLASS_NAME, 'inventory_item')
    products = wait.until(EC.visibility_of_all_elements_located(products_locator))
    for product in products:
        product: WebElement
        name = product.find_elements_by_class_name('inventory_item_name')
        price = product.find_elements_by_class_name('inventory_item_price')
        result.append(f'Name: {name.text}, Price: {price.text}')
    return result


if __name__ == '__main__':
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/index.html')
    login(wait, 'standard_user', 'secret_sauce')
    print(get_catalog_info(wait))
    driver.quit()
