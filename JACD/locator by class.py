import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/intl/es-419/gmail/about/#")
search = driver.find_element_by_class_name("h-c-button").click();
time.sleep(5)
#driver.quit()
