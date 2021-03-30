from Common.webdriver_factory import  get_driver

driver = get_driver('chrome')

driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&dsh=S-754881558%3A1613063574131574&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')
nombre = driver.find_element_by_id('firstName')
nombre.clear()
nombre.send_keys('Rodrigo')

apellido = driver.find_element_by_id('lastName')
apellido.clear()
apellido.send_keys('Mejia')

usuario = driver.find_element_by_id('username')
usuario.clear()
usuario.send_keys('userusers8990')

contra = driver.find_element_by_name('Passwd')
contra.clear()
contra.send_keys('Qw3rty78iop')

confirma = driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
confirma.clear()
confirma.send_keys('Qw3rty78iop')

siguiente = driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button')
siguiente.click()

telefon = driver.find_element_by_id('phoneNumberId')
telefon.clear()
telefon.send_keys('3345677654')

driver.quit()