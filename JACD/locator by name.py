import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
#print(driver.title)

#search = driver.find_element_by_id('tophf')
#search= driver.find_element_by_class_name('gLFyf gsfi')
search = driver.find_element_by_name('q')
driver.implicitly_wait(10)
driver.maximize_window()
search.send_keys('accenture')
search.send_keys(Keys.ENTER)
driver.implicitly_wait(20)
driver.close()
