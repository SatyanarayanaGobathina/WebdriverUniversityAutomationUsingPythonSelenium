import time

from selenium.webdriver.common.by import By

from BaseDriver import driver


driver.get('http://webdriveruniversity.com/IFrame/index.html')
driver.switch_to.frame('frame')
driver.find_element(By.LINK_TEXT,'Our Products').click()
driver.find_element(By.ID,'new-laptops').click()
time.sleep(5)
print(driver.find_element(By.XPATH,"//div[@id='myModal']/div/div/div[2]/p").text)
driver.find_element(By.XPATH,'//*[@id="myModal"]/div/div/div[3]/button[2]').click()
time.sleep(5)
driver.close()