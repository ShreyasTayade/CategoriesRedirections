from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//shreyas.tayade//Downloads//chromedriver_win32.exe")

driver.get("https://vet.medikabazaar.com/account/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys("Shreyas.tayade15@gmail.com")
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[3]/div/form/button").click()

