import time
from selenium.webdriver.common.by import By
from BaseDriver import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver.get("http://webdriveruniversity.com/Click-Buttons/index.html")
driver.maximize_window()
# implicit wait
# driver.implicitly_wait(10)
# driver.find_element(By.ID,'button1').click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,'button[data-dismiss="modal"]').click()

# explicit wait
wait = WebDriverWait(driver,10)
button1 = wait.until(EC.presence_of_element_located((By.ID,'button1')))
button1.click()
time.sleep(5)

# driver.find_element(By.CSS_SELECTOR,'button[data-dismiss="modal"]').click()
close_button = driver.find_element(By.CSS_SELECTOR,'button[data-dismiss="modal"]')
close_button.click()
