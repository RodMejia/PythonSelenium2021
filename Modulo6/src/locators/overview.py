from selenium.webdriver.common.by import By

class OverPageLoc:

    TITLE = (By.CLASS_NAME, 'title')
    ITEMS = (By.CLASS_NAME, 'cart_item')
    SUB_TOTAL = (By.CLASS_NAME, 'summary_subtotal_label')
    TAX = (By.CLASS_NAME, 'summary_tax_label')
    TOTAL = (By.CLASS_NAME, 'summary_total_label')
    BACK = (By.XPATH, "//button[contains(@class,'btn_medium')]")
    FINISH = (By.XPATH, "//button[contains(@class,'btn_action')]")