from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from Common.webdriver_factory import get_driver


def first_logbutton(wait: WebDriverWait):
    locator = (By.XPATH, "//*[@data-test-id = 'simple-login-button']")
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()


def enter_credentials(wait: WebDriverWait, user: str, passwd: str):
    locator = (By.ID, "email")
    user_element = wait.until(EC.element_to_be_clickable(locator))
    user_element.send_keys(user)

    locator2 = (By.ID, "password")
    pass_element = wait.until(EC.element_to_be_clickable(locator2))
    pass_element.send_keys(passwd)

    locator3 = (By.XPATH, "//*[@data-test-id='registerFormSubmitButton']")
    button_element = wait.until(EC.element_to_be_clickable(locator3))
    button_element.click()


def enter_search(wait: WebDriverWait, search_text: str):
    locator = (By.NAME, "searchBoxInput")
    searchbox_element = wait.until(EC.element_to_be_clickable(locator))
    searchbox_element.send_keys(search_text)
    searchbox_element.send_keys(Keys.ENTER)


def get_results(wait: WebDriverWait):
    gettags_locator = (By.XPATH, "//*[@data-test-id = 'search-guide']")
    tags_element = wait.until(EC.visibility_of_all_elements_located(gettags_locator))
    for element in tags_element:
        print(element.text)



if __name__ == '__main__':

    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)

    driver.get('https://www.pinterest.com.mx')

    first_logbutton(wait)

    enter_credentials(wait, 'qamindstester@gmail.com', 'Q@Minds4%')

    enter_search(wait, 'selenium')

    get_results(wait)

    driver.quit()