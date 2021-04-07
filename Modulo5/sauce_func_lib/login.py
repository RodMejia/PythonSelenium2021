from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from module_05.sauce_func_lib.common import write_to_input, click, get_text


def login(wait: WebDriverWait, user: str, password: str):
    write_to_input(wait, (By.ID, 'user-name'), user)
    write_to_input(wait, (By.ID, 'password'), password)
    click(wait, (By.ID, 'login-button'))


def get_login_error(wait: WebDriverWait) -> str:
  
    locator = (By.XPATH, "//*[@data-test='error']")
    return get_text(wait, locator)