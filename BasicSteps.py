import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



service = Service(r"C://selenium web drivers/geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.get("http://webdriveruniversity.com/index.html")
driver.maximize_window()
#links = driver.find_elements(By.TAG_NAME,'a')
time.sleep(5)
# mywait = WebDriverWait(driver,20)
# element = mywait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="CONTACT US"]')))
# element.click()
