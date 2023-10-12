import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

# var = selenium.webdriver.support.wait
import time

options = webdriver.ChromeOptions()


options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


# To get Website
driver.get("https://www.medikabazaar.com/account")

# To maximize the browser
driver.maximize_window()


# To Login With user
driver.find_element(By.NAME, "email").send_keys("freuneuraufougru-8898@yopmail.com")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.implicitly_wait(5)

# time.sleep(3)

# To Send password
driver.find_element(By.NAME,"password").send_keys("Shreyas@15")
# time.sleep(5)
driver.implicitly_wait(5)

# click on submit
driver.find_element(By.XPATH,"//*[@id='__next']/div/div/div/div/form/button[1]").click()
driver.implicitly_wait(5)

# time.sleep(5)

# click on Medikabazaar to redirect to Home page
driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/img[1]").click()


# select consumable
driver.find_element(By.XPATH,"//img[@alt='consumables']").click()
driver.implicitly_wait(5)

current_url = driver.current_url

if current_url=="https://www.medikabazaar.com/consumables":
    print("Consumable Redirection Passed")
else:
    print("Consumables Failed")
