from selenium.webdriver.common.by import By

from BaseDriver import driver


driver.get('https://www.dummyticket.com/dummy-ticket.for-visa-application/')
driver.find_element(By.XPATH,'//span[@id="select2-billing_country-container"]').click()
countriesList = driver.find_elements(By.XPATH,'//ul[@id="select2-billing_country-results"]/li')
print(len(countriesList))
for x in countriesList:
    if x.text=='India':
        x.click()
        break
driver.get_screenshot_as_file('India.png')
driver.close()