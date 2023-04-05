import time

from BaseDriver import driver

driver.implicitly_wait(10)
driver.get('https://wn.com/Countries-of-the-world')
driver.execute_script('window.scrollBy(0,3000)','')
value = driver.execute_script('return window.pageYOffset;')
print(value)
time.sleep(5)
driver.execute_script('window.scrollBy(0,-document.body.scrollHeight)')
value = driver.execute_script('return window.pageYOffset;')
print(value)



driver.close()