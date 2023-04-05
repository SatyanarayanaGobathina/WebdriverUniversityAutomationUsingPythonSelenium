import time
import requests

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
links = driver.find_elements(By.XPATH,'//a')
print(len(links))
time.sleep(5)
count =0
for link in links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, 'is broken')
        count = +1
    else:
        print(url,'is valid')
print('total dead links are', count)



print(driver.close())