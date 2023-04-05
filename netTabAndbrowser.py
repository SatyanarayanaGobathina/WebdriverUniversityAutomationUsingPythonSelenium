import time

from selenium.webdriver.common.by import By

from BaseDriver import driver
from selenium.webdriver.common.keys import Keys

driver.get('http://webdriveruniversity.com/index.html')
new = Keys.CONTROL+Keys.RETURN
driver.find_element(By.LINK_TEXT,'Selenium Webdriver 4 New Features In Detail').send_keys(new)
tabs = driver.window_handles
driver.switch_to.window(tabs[1])
driver.switch_to.new_window('tab')
driver.get('https://ultimateqa.com/dummy-automation-websites/')
driver.switch_to.new_window('window')
driver.get('https://ultimateqa.com/dummy-automation-websites/')
time.sleep(5)
driver.close()
time.sleep(5)
driver.quit()