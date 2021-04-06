from Common.webdriver_factory import get_driver

driver = get_driver('chrome')

driver.implicitly_wait(10)

driver.get('https://www.google.com')

firstdiv_hijo = driver.find_element_by_xpath('//body//div')
print(firstdiv_hijo.text)

lastdiv_hijo = driver.find_element_by_xpath('//body//div[last()]')
print(lastdiv_hijo.text)

primer_role = driver.find_element_by_xpath('//script[@role = "navigation"]')
print(primer_role.text)

nav_class = driver.find_element_by_xpath('//body[@class = "nav"]')
print(nav_class.text)

submit_type = driver.find_element_by_xpath('//*[@type = "submit"]')
print(submit_type.text)