from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from Common.webdriver_factory import get_driver


def search(wait: WebDriverWait, value: str):
    """Search in tiktok
    :param wait: Web driver instance
    :param value: search string
    """

    locator = (By.NAME, "q")
    search_textbox = wait.until(EC.element_to_be_clickable(locator))
    search_textbox.clear()
    search_textbox.send_keys(value)
    search_textbox.send_keys(Keys.ENTER)


def print_results(wait: WebDriverWait):
    profiles_loc = (By.XPATH, "//a[contains(@class, 'result-item')]")
    rows = wait.until(EC.visibility_of_all_elements_located(profiles_loc))
    for row in rows:
        print(parse_user_info(wait, row))


def parse_user_info(wait: WebDriverWait, row: WebElement):
    """Parse user info."""
    title = row.find_element_by_xpath(".//*[contains(@class, ' title ')]")
    sub_title = row.find_element_by_xpath(".//*[contains(@class, 'sub-title')]")
    description = row.find_element_by_xpath(".//*[contains(@class, 'desc')]")
    return f'{title.text:20} | {sub_title.text:20} | {description.text:20}'


if __name__ == '__main__':
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 3)

    my_driver.get('https://www.tiktok.com/?lang=es')

    search(my_wait, 'Python')

    print_results(my_wait)

    my_driver.quit()