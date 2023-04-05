import time

from BaseDriver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver.get('http://webdriveruniversity.com/Actions/index.html#')
#drag and drop
source = driver.find_element(By.ID,'draggable')
target = driver.find_element(By.ID,'droppable')
act = ActionChains(driver)
act.drag_and_drop(source,target).perform()
time.sleep(2)
# double click
doubleClick = driver.find_element(By.ID,'double-click')
act.double_click(doubleClick).perform()
time.sleep(2)
# mouse hover and link click, switch to alert and accept
mh1 = driver.find_element(By.XPATH, "//button[text()='Hover Over Me First!']")
act.move_to_element(mh1).perform()
driver.find_element(By.XPATH, "//div[@id='div-hover']/div[1]/div/a").click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()
# mouse hover2
mh2 = driver.find_element(By.XPATH,"//button[text()='Hover Over Me Second!']")
link1 = driver.find_element(By.XPATH, "//div[@id='div-hover']/div[2]/div/a")
act.move_to_element(mh2).move_to_element(link1).click().perform()
alert = driver.switch_to.alert
alert.accept()
#mouse hover3, link 2
# mouse hover2
mh3 = driver.find_element(By.XPATH,"//button[text()='Hover Over Me Third!']")
link2 = driver.find_element(By.XPATH, "//div[@id='div-hover']/div[3]/div/a[2]")
act.move_to_element(mh3).move_to_element(link2).click().perform()
time.sleep(3)
alert = driver.switch_to.alert
alert.accept()

time.sleep(3)
#long left click and hold
longClick = driver.find_element(By.XPATH,'//div[@id="click-box"]/p')
act.click_and_hold(longClick).perform()
time.sleep(3)

# right cick
header = driver.find_element(By.ID,'main-header')
act.context_click(header).perform()

driver.close()
driver.quit()