import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service = Service(r"C://selenium web drivers/geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.get("http://webdriveruniversity.com/Contact-Us/contactus.html")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[name=first_name]").send_keys('firstname')
driver.find_element(By.CSS_SELECTOR,"input[name=last_name]").send_keys('lastname')
driver.find_element(By.CSS_SELECTOR,"input.feedback-input[name=email]").send_keys('samplemail.com')
driver.find_element(By.CSS_SELECTOR,"textarea.feedback-input[name=message]").send_keys('customised css celectors')

driver.find_element(By.XPATH,"//div[@id='form_buttons']/input[2]").click()
assert driver.find_element(By.TAG_NAME,'body').text == 'Error: Invalid email address'
driver.close()