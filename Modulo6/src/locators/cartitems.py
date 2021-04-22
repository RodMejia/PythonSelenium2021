from selenium.webdriver.common.by import By

class CartItemLoc:

    TITLE = (By.CLASS_NAME, 'inventory_item_name')
    DESCRIPTION = (By.CLASS_NAME, 'inventory_item_desc')
    PRICE = (By.CLASS_NAME, 'inventory_item_price')
    REM_BTN = (By.XPATH, ".//button[contains(@class,'cart_button')]")


