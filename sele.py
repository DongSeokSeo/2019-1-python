from selenium import webdriver

driver = webdriver.Chrome('D:\서동석\chromedriver_win32\chromedriver')
driver.implicitly_wait(10)

driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('sds6952')
driver.find_element_by_name('pw').send_keys('tjtj69526952!!')

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


 

