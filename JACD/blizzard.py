from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.blizzard.com/en-us/")
search = driver.find_element_by_class_name("container--2ucK6").click();
#time.sleep(5)
#driver.quit()
