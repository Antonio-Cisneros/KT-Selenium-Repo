from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youtube.com/")
driver.find_element_by_id('button').click()
#time.sleep(5)
#driver.quit()
