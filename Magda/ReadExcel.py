import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

url = driver.find_element(By.ID, "Form_submitForm_subdomain")
name = driver.find_element(By.ID, "Form_submitForm_Name")
email = driver.find_element(By.ID, "Form_submitForm_Email")
phone_number = driver.find_element(By.ID,"Form_submitForm_Contact")
country = driver.find_element(By.ID, "Form_submitForm_Country")

workbook = xlrd.open_workbook("DataFile.xls")
sheet = workbook.sheet_by_name("registration")

# get total number of rows: 
rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    url = sheet.cell_value(curr_row,0)
    name = sheet.cell_value(curr_row,1)
    email = sheet.cell_value(curr_row,2)
    phoneNumber = sheet.cell_value(curr_row,3)
    country = sheet.cell_value(curr_row,4)

print(url + name + email)