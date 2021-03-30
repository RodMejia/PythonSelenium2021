from Common.webdriver_factory import get_driver

driver = get_driver('chrome')
datos = ['Rodrigo','Mejia','rmejia@anexinet.com','Support Inquiry','Texto loco, ese']

driver.get('https://formsmarts.com/html-form-example')
driver.switch_to.frame(driver.find_element_by_class_name('fs_embed'))

firstname = driver.find_element_by_xpath('//*[@id="u_2wi_4607"]')
firstname.clear()
firstname.send_keys(datos[0])

lastname = driver.find_element_by_xpath('//*[@id="u_2wi_338354"]')
lastname.clear()
lastname.send_keys(datos[1])

email = driver.find_element_by_xpath('//*[@id="u_2wi_4608"]')
email.clear()
email.send_keys(datos[2])

click_inquiry = driver.find_element_by_xpath('//*[@id="u_2wi_338367"]')
click_inquiry.click()

select_inquiry = driver.find_element_by_xpath('/html/body/div/form/select/option[3]')
select_inquiry.click()

inquiry_text = driver.find_element_by_xpath('//*[@id="u_2wi_4609"]')
inquiry_text.clear()
inquiry_text.send_keys(datos[4])

continue_button = driver.find_element_by_xpath('/html/body/div/form/div/input')
continue_button.click()

if driver.current_url == 'https://formsmarts.com/html-form-example':
    if datos[0] in driver.page_source:
        print(f'Name found')
    if datos[1] in driver.page_source:
        print(f'Last name found')
    if datos[2] in driver.page_source:
        print(f'Email found')
    if datos[3] in driver.page_source:
        print(f'Inquiry found')
    if datos[4] in driver.page_source:
        print(f'Comments found')

driver.quit()