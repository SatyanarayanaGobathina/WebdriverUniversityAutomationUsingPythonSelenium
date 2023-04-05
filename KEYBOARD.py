from BaseDriver import driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver.get('http://webdriveruniversity.com/To-Do-List/index.html')
act = ActionChains(driver)
key = Keys
input = driver.find_element(By.XPATH,'//*[@id="container"]/input')
input.send_keys('interview scheduled for tomorrow morning 9am')
act.key_down(key.CONTROL)
act.send_keys('a')
data = act.send_keys('c')
print(data)
act.key_up(key.CONTROL)
act.key_down(key.ENTER)
act.key_up(key.ENTER)
act.perform()
act.key_down(key.CONTROL)
act.send_keys('v')
act.key_up(key.CONTROL).perform()
act.key_down(key.ENTER)
act.key_up(key.ENTER)
act.perform()
#trash
delete = driver.find_element(By.XPATH,'/html/body/div/ul/li[2]/span/i')
act.move_to_element(delete).click().perform()

#driver.close()
