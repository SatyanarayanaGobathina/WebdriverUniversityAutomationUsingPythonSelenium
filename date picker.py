from selenium.webdriver.common.by import By
from BaseDriver import driver


driver.get('https://jqueryui.com/datepicker/')
frame = driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(frame)
driver.find_element(By.ID,'datepicker').send_keys('01/27/2023')
x = eval(input('enter:'))
