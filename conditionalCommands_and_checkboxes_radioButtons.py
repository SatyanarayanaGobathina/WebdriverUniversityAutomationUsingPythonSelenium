import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



service = Service(r"C://selenium web drivers/geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.get("http://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
driver.maximize_window()
print(driver.title)
pg = driver.page_source
header = driver.find_element(By.XPATH,'//div[@id="main-header"]')
print('header displayed?--', header.is_displayed())
print('header enabled?--', header.is_enabled())
checkbox = driver.find_element(By.XPATH,"//div[@id='checkboxes']/label[3]/input")
print(checkbox.is_selected())
selecting_all_checkboxes=driver.find_elements(By.XPATH,"//div[contains(@id,'checkboxes')]/label")
print(len(selecting_all_checkboxes),selecting_all_checkboxes[2].is_selected())
for x in selecting_all_checkboxes:
    if  x.is_selected()==True:
       pass
    else:
        x.click()
time.sleep(5)
#dropdown
dropdown=driver.find_element(By.CLASS_NAME,'dropdown-menu-lists')
#dropdown=driver.find_element(By.XPATH,"select[class='dropdown-menu-lists']")
selectOne= Select(dropdown)
selectOne.select_by_visible_text('Python')
names = selectOne.options
for x in names:
    print(x.text)
all = driver.find_elements(By.XPATH,'//div[@class="container"]/div[5]/div/div/form/input')
print(len(all))
for x in all:
    if x.is_enabled():
        None
    else:
        print(x.get_attribute('value'),'is disabled')
        





driver.close()
