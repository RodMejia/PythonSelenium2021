from Common.webdriver_factory import  get_driver

driver = get_driver('chrome')


driver.get('https://www.selenium.dev/')
print(f'Current title: {driver.title}')
print(f'Current URL: {driver.current_url}')
element1 = driver.find_element_by_link_text('Downloads')
if element1.is_displayed():
    print(f'Is displayed')
if element1.is_enabled():
    print(f'Is enabled')
if element1.is_selected():
    print(f'Is selected')
driver.quit()
#actividad 2.4 y 2.5



