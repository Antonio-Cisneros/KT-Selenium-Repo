import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/intl/es-419/gmail/about/#")
driver.maximize_window()
search= driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a").click();
time.sleep(5)
driver.quit()


#driver.findElement(By.id("signupModalButton")).click(); //using Selenium click button method