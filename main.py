from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver_service = Service("C:/chromedriver_win32/chromdriver.exe")
driver = webdriver.Chrome(service = driver_service)

driver.get("https://www.google.com/")

searchbar = driver.find_element(By.CLASS_NAME, "gLFyf")
searchbar.send_keys("Dota 2")




