from selenium.webdriver.common.by import By

class CartPageLoc:

    ITEMS = (By.CLASS_NAME, 'cart_item')
    TITLE = (By.CLASS_NAME, 'title')
    BACK = (By.XPATH, "//button[contains(@class,'btn_medium')]")
    CHK_BTN = (By.XPATH, "//button[contains(@class,'checkout_button')]")