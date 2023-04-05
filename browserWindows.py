from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

service = Service(r"C://selenium web drivers/geckodriver.exe")
options = Options()
options.headless = True
options.set_preference("dom.push.enabled", False)

driver = webdriver.Firefox(service=service,options=options)
driver.get("https://ultimateqa.com/dummy-automation-websites/")
windowId = driver.current_window_handle
print(windowId)
print(type(windowId))
driver.find_element(By.LINK_TEXT,'E-commerce Clothing Site').click()
all_windows = driver.window_handles
print(type(all_windows))
parentWindow = all_windows[0]
print(type(parentWindow))
childWindow = all_windows[1]
driver.switch_to.window(parentWindow)
print(driver.title)

driver.close()