from selenium import webdriver
import time
 
browser = webdriver.Chrome('D:\서동석\chromedriver_win32\chromedriver')
browser.get("http://python.org")
 
menus = browser.find_elements_by_css_selector('#top ul.menu li')
 
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)
 
pypi.click()  
 
time.sleep(5) 
browser.quit() 
