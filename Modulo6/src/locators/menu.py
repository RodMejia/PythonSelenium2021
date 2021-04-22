from selenium.webdriver.common.by import By


class MenuLoc:

    ALL_ITEMS = (By.ID, 'inventory_sidebar_link')
    ABOUT = (By.ID, 'about_sidebar_link')
    LOGOUT = (By.ID, 'logout_sidebar_link')
    BURGER_BTN = (By.CLASS_NAME, 'bm-burger-button')