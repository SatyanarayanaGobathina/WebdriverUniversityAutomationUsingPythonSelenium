from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def driver_metod():
    service = Service(r"C://selenium web drivers/geckodriver.exe")
    driver= webdriver.Firefox(service=service)
    driver.maximize_window()
    return driver

driver = driver_metod()
