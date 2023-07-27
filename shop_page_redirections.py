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

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

# driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(3)

# driver.find_element(By.ID, 'file-upload').send_keys("c:\\Screenshot.png")


# driver.find_element(By.ID, 'file-submit').click()
# driver = webdriver.Chrome(executable_path="C://Users//shreyas.tayade//Downloads//chromedriver_win32.exe")

# driver.get("https://vet.medikabazaar.com/account/login")
# driver.maximize_window()
#
# time.sleep(5)

# driver.find_element(By.NAME, "email").send_keys("Shreyas.tayade15@gmail.com")

# time.sleep(3)

# driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[3]/div/form/button").click()

# driver.find_element(By.NAME, "code").send_keys("Shreyas@15")

# driver.find_element(By.CLASS_NAME, "w-full bg-[#EC6303] text-sm font-semibold text-[#FFFFFF] py-[17px] rounded-sm undefined").click()

# time.sleep(5)




from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch the web browser
options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome(executable_path="C://Users//shreyas.tayade//Downloads//chromedriver_win32.exe")

# To get on Website
# driver.get("https://dental.medikabazaar.com/account")

# driver.maximize_window()
# time.sleep(3)

# driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/button[1]").click()
#
# driver.find_element(By.XPATH,'//*[@placeholder="eg. johndoe@gmail.com"]').send_keys("freuneuraufougru-8898@yopmail.com")






# To Login With user

# driver.find_element(By.NAME, "email").send_keys("freuneuraufougru-8898@yopmail.com")

# driver.find_element(By.XPATH,"//button[@type='submit']").click()

# time.sleep(3)

# To Send password
# driver.find_element(By.NAME,"password").send_keys("Shreyas@15")
# time.sleep(5)

# click on submit
# driver.find_element(By.XPATH,"//*[@id='__next']/div/div/div/div/form/button[1]").click()

# time.sleep(5)

# click on Medikabazaar to redirect to Home page
# driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/img[1]").click()

driver.get("https://www.medikabazaar.com/shop")

driver.maximize_window()

# select consumable
driver.find_element(By.XPATH,"//img[@alt='consumables']").click()
driver.implicitly_wait(5)

current_url = driver.current_url

if current_url=="https://www.medikabazaar.com/consumables":
    print("Consumable Redirection Passed")
else:
    print("Consumables Failed")


# Go on Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()

driver.implicitly_wait(5)

# select dental
driver.find_element(By.XPATH,"//img[contains(@alt, 'dental')]").click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental":
    print("Dental Redirection Passed")
else:
    print("Dental Failed")

# Go on Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()

# select Vet
driver.find_element(By.XPATH,'//img[@alt="veterinary"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary":
    print("Veterinary Redirection Passed")
else:
    print("veterinary Failed")

# Go on Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()


# select diagnostics
driver.find_element(By.XPATH,'//img[@alt="diagnostics"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics":
    print("Diagnostics Redirection Passed")
else:
    print("Diagnostics Failed")

# Go on Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()

# select diagnostics
driver.find_element(By.XPATH,'//img[@alt="physiotherapy"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/physiotherapy":
    print("Physiotherapy Redirection Passed")
else:
    print("Physiotherapy Failed")


# Go on Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()


# select medicalequipment
driver.find_element(By.XPATH,'//img[@alt="medicalequipments"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments":
    print("Medical Device & Equipments Redirection Passed")
else:
    print("Medical Device & Equipments Failed")


# Go on Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()

driver.implicitly_wait(5)



# select Nexage
driver.find_element(By.XPATH,'//div[7]/a[1]/div[1]/img[1]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental/products?collection_slug=nexage":
    print("Nexage Redirection Passed")
else:
    print("Nexage Failed")



time.sleep(4)

# Go on Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()


driver.implicitly_wait(5)


# select top offers
driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/a[1]/div[1]/img[1]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/products?collection_slug=top-offers":
    print("Top Offers Redirection Passed")
else:
    print("Top Offers Failed")


# Go on Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()

current_url = driver.current_url


if current_url == "https://www.medikabazaar.com/shop":
    print("Home page Categories Redirection Passed")
else:
    print("Home page Categories Redirection Failed")







#
# # Add to Cart product
# driver.find_element(By.XPATH,"//*[@id='addToCart']/span[1]").click()
# driver.implicitly_wait(5)
# time.sleep(6)
#
# #
# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/button[2]/div[2]").click()
# #
# driver.implicitly_wait(5)
#
# driver.find_element(By.XPATH,'//button[@type="button"]').click()
#
#
# # driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/button[1]").click()
# #
# driver.implicitly_wait(7)
#
# driver.find_element(By.XPATH,'//div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/button[1]').click()
# # driver.find_element(By.XPATH,"//div[2]/div[1]/div[1]/div[2]/button[1]").click()
# #
# # time.sleep(3)
# #
# driver.find_element(By.XPATH,"//div[7]/div[2]/button[1]").click()
# #
# # time.sleep(3)
# #
# driver.find_element(By.XPATH,"//div[5]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]").click()
#
#
#
#

# # Navigate to the login page


# browser.get('https://vet.medikabazaar.com/account/login')
#
# browser.find_element(By.NAME, "email").send_keys("Shreyas.tayade15@gmail.com")
#
# # browser.find_element_by_name('email').send
#
# # Locate the email and password input fields
# email_field = browser.find_element_by_name('email')
# password_field = browser.find_element_by_name('password')
#
# # Input the email and password credentials
# email_field.send_keys('Shreyas.tayade15@gmail.com')
# password_field.send_keys('Shreyas@15')
#
# # Simulate clicking the login button
# login_button = browser.find_element_by_xpath("//button[@type='submit']")
# login_button.click()
#
# # Wait for the dashboard page to load
# browser.implicitly_wait(10)
#
# # Print the title of the dashboard page
# print(browser.title)
#
# # Close the browser
# browser.quit()
