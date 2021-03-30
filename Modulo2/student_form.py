from Common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select

FIRST_NAME = 'Rodrigo'
LAST_NAME = 'Mejia'
EMAIL = 'rmejia@anexinet.com'
ADDRESS = 'Chanxopan 102'
COUNTRY = 'MX'
CURRENT_DATE = '02 / 15 / 2021'
NO_NIGHTS = '4'

driver = get_driver('chrome')
driver.get('https://formsmarts.com/form/axi?mode=h5')

first_name = driver.find_element_by_id('u_LY9_60857')
first_name.send_keys(FIRST_NAME)

last_name = driver.find_element_by_id('u_LY9_60858')
last_name.send_keys(LAST_NAME)

email = driver.find_element_by_id('u_LY9_60859')
email.send_keys(EMAIL)

address = driver.find_element_by_id('u_LY9_60860')
address.send_keys(ADDRESS)

country = driver.find_element_by_id('u_LY9_60871')
dropdown = Select(country)
dropdown.select_by_value(COUNTRY)

current_date = driver.find_element_by_id('u_LY9_60861')
current_date.clear()
current_date.send_keys(CURRENT_DATE)

room = driver.find_element_by_xpath('/html/body/div/form/fieldset/label[3]/span')

no_nights = driver.find_element_by_xpath('//*[@id="u_LY9_60870"]')
no_nights.send_keys(NO_NIGHTS)

continue_button = driver.find_element_by_xpath('/html/body/div/form/div[2]/input')
continue_button.click()

#https://docs.python.org/3/library/datetime.html

driver.quit()

