
from selenium.webdriver import ActionChains
import mouseActions
from BaseDriver import driver
from selenium.webdriver.common.by import By


driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')
minSlider = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/span[1]")
maxSlider = driver.find_element(By.XPATH,"/html/body//div[2]/div[2]/span[2]")
print(minSlider.location,maxSlider.location)
act = ActionChains(driver)
act.move_to_element_with_offset(minSlider,149,0).perform()
act.move_to_element_with_offset(maxSlider,50,0).perform()
print(minSlider.location,maxSlider.location)
driver.close()