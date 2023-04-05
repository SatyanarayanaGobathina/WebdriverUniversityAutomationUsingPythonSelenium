from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service = Service(r"C://selenium web drivers/geckodriver.exe")
driver= webdriver.Firefox(service=service)
driver.maximize_window()
driver.get("http://webdriveruniversity.com/Click-Buttons/index.html")
driver.implicitly_wait(2)
driver.find_element(By.ID,'button1').click()
driver.find_element(By.CSS_SELECTOR,'button[data-dismiss="modal"]').click()
time.sleep(2)
b2=driver.find_element(By.CSS_SELECTOR,"span[id='button2']")
driver.execute_script("arguments[0].click();",b2)
time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="myModalJSClick"]/div/div/div[3]/button').click()
time.sleep(2)
b3 = driver.find_element(By.XPATH,'//span[@id="button3"]')
act = ActionChains(driver)
act.move_to_element(b3).click(b3).perform()


#element= mywait.until(EC.presence_of_element_located())
