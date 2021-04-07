from selenium.webdriver.support.wait import WebDriverWait
from Common.webdriver_factory import get_driver
from Modulo5.sauce_func_lib.Inventory import get_inventory, InventoryItem
from Modulo5.sauce_func_lib.login import login


VALID_PRICE = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']


def test_inventory_size():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    assert len(items) == 6, 'Inventory should contain 6 items'
    driver.close()


def test_inventory_prices():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    for index, item in enumerate(items):
        item: InventoryItem
        assert item.price == VALID_PRICE[index], f'Price for item {index} should be {VALID_PRICE[index]}'
    driver.close()