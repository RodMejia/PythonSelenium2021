from selenium.webdriver.common.by import By

class ChkOutPageLoc:
    TITLE = (By.CLASS_NAME, 'title')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CANCEL = (By.XPATH, "//button[contains(@class,'btn_secondary')]")
    CONTINUE = (By.ID, 'continue')