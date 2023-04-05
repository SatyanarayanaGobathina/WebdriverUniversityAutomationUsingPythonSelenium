from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(r"C://selenium web drivers/geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.get('http://webdriveruniversity.com/Popup-Alerts/index.html')
driver.find_element(By.XPATH, "//span[@onclick='myFunction()']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(5)
driver.execute_script('document.getElementById("button2").click()')
time.sleep(5)

driver.find_element(By.XPATH,'//button[@data-dismiss="modal"]').click()
time.sleep(5)
driver.find_element(By.ID,'button4').click()
time.sleep(5)
alert2 = driver.switch_to.alert
time.sleep(5)
alert2.dismiss()
# Authentication popup----we need to bypass the url
driver.find_element(By.ID,'button3').click()
time.sleep(5)
driver.find_element(By.ID,'button1').click()
time.sleep(5)
driver.find_element(By.XPATH,'//button[@data-dismiss="modal"]').click()


driver.quit()