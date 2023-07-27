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
driver.get("https://www.medikabazaar.com/shop")

driver.maximize_window()

# To Login With user
# driver.find_element(By.NAME, "email").send_keys("freuneuraufougru-8898@yopmail.com")
#
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# time.sleep(3)
#
# # To Send password
# driver.find_element(By.NAME, "password").send_keys("Shreyas@15")
# time.sleep(5)
#
# # click on submit
# driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div/div/form/button[1]").click()
#
# time.sleep(5)

# click on Medikabazaar to redirect to Home page
# driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/img[1]").click()

# select consumable
driver.find_element(By.XPATH, "//img[@alt='consumables']").click()
driver.implicitly_wait(5)

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/consumables":
    print("Consumable Redirection --> Passed")
else:
    print("Consumables --> Failed")


# To open general consumable and disposables
driver.find_element(By.XPATH,'//*[contains(@alt, "general-consumable-and-disposables")]').click()

current_url = driver.current_url


if current_url == "https://www.medikabazaar.com/consumables/specialities/general-consumable-and-disposables":
    print("General Consumable and Disposables Redirection --> Passed")
else:
    print("General Consumable and Disposables Redirection --> Failed")

driver.back()

# To open cardiology
driver.find_element(By.XPATH,'//img[contains(@alt, "cardiology")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/consumables/specialities/cardiology":
    print("Cardiology Redirection --> Passed")
else:
    print("Cardiology Redirection --> Failed")

driver.back()

# To open respiratory
driver.find_element(By.XPATH,'//img[contains(@alt, "respiratory")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/consumables/specialities/respiratory":
    print("Respiratory Redirection --> Passed")
else:
    print("Respiratory Redirection --> Failed")

driver.back()


# To open Urology
driver.find_element(By.XPATH,'//img[contains(@alt, "urology")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/consumables/specialities/urology":
    print("Urology Redirection --> Passed")
else:
    print("Urology Redirection --> Failed")

driver.back()




# To open wound-care-and-dressing
driver.find_element(By.XPATH,'//img[contains(@alt, "wound-care-and-dressing")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/consumables/specialities/wound-care-and-dressing":
    print("wound-care-and-dressing Redirection --> Passed")
else:
    print("wound-care-and-dressing Redirection --> Failed")

driver.back()


# To open Suture
driver.find_element(By.XPATH,'//img[contains(@alt, "suture")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/consumables/specialities/suture":
    print("Suture Redirection --> Passed")
else:
    print("Suture Redirection --> Failed")

driver.back()

# To open Hospital Apparel and Personal Protection
driver.find_element(By.XPATH,'//img[contains(@alt, "hospital-apparel-and-personal-protection")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/consumables/specialities/hospital-apparel-and-personal-protection":
    print("Hospital Apparel and Personal Protection Redirection  -->Passed")
else:
    print("Hospital Apparel and Personal Protection Redirection  -->Failed")

driver.back()

# To open Gynecology & Obstetrics
driver.find_element(By.XPATH,'//img[contains(@alt, "gynecology-obstetrics")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/consumables/specialities/gynecology-obstetrics":
    print("Gynecology & Obstetrics Redirection --> Passed")
    print("Consumables & Disposables Categories Redirections --> Passed")
else:
    print("Gynecology & Obstetrics Redirection --> Failed")

driver.back()

# Go to Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()

# select dental
driver.find_element(By.XPATH,"//img[contains(@alt, 'dental')]").click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental":
    print("Dental Redirection --> Passed")
else:
    print("Dental Failed")


# To open Endodontics
driver.find_element(By.XPATH,'//img[contains(@alt, "endodontics")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental/specialities/endodontics":
    print("Endodontics Redirection --> Passed")

else:
    print("Endodontics Redirection --> Failed")

driver.back()


# To open Restorative Materials
driver.find_element(By.XPATH,'//img[contains(@alt, "restorative-materials")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental/categories/restorative-materials":
    print("Restorative Materials Redirection --> Passed")

else:
    print("Restorative Materials Redirection --> Failed")

driver.back()

# To open Consumables
driver.find_element(By.XPATH,'//img[contains(@alt, "consumables")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental/categories/consumables":
    print("Consumables Redirection --> Passed")

else:
    print("Consumables Redirection --> Failed")

driver.back()

# To open Prosthodontics
driver.find_element(By.XPATH,'//img[contains(@alt, "prosthodontics")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental/specialities/prosthodontics":
    print("Prosthodontics Redirection --> Passed")

else:
    print("Prosthodontics Redirection --> Failed")

driver.back()

# To open Orthodontics & Dentofacial Orthopedics
driver.find_element(By.XPATH,'//img[contains(@alt, "orthodontics-dentofacial-orthopedics")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental/specialities/orthodontics-dentofacial-orthopedics":
    print("Orthodontics & Dentofacial Orthopedics Redirection --> Passed")

else:
    print("Orthodontics & Dentofacial Orthopedics Redirection --> Failed")

driver.back()

# To open Dental Equipment
driver.find_element(By.XPATH,'//img[contains(@alt, "dental-equipment")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental/categories/dental-equipment":
    print("Dental Equipment Redirection --> Passed")

else:
    print("Dental Equipment Redirection --> Failed")

driver.back()


# To open Periodontics
driver.find_element(By.XPATH,'//img[contains(@alt, "periodontics")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental/specialities/periodontics":
    print("Periodontics Redirection --> Passed")

else:
    print("Periodontics Redirection --> Failed")

driver.back()


# To open Dental Instruments
driver.find_element(By.XPATH,'//img[contains(@alt, "dental-instruments")]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/dental/categories/dental-instruments":
    print("Dental Instruments Redirection --> Passed")
    print("Dental categories Redirection --> Passed")

else:
    print("Dental Instruments Redirection --> Failed")

driver.back()



# Go to Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()

#To Open Veterinary

driver.find_element(By.XPATH,'//img[contains(@alt, "veterinary")]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary":
    print("Veterinary Redirection --> Passed")

else:
    print("Veterinary Redirection --> Failed")




#To open  Vet Consumable & Disposable
driver.find_element(By.XPATH,'//img[@alt="vet-consumable-disposable"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary/categories/vet-consumable-disposable":
    print("Vet Consumable & Disposable Redirection --> Passed")

else:
    print("Vet Consumable & Disposable Redirection --> Failed")
driver.back()



#To open  Vet Devices & Equipment
driver.find_element(By.XPATH,'//img[@alt="vet-devices-equipment"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary/categories/vet-devices-equipment":
    print("Vet Devices & Equipment Redirection --> Passed")

else:
    print("Vet Devices & Equipment Redirection --> Failed")
driver.back()


#To open  Vet-pharma-store
driver.find_element(By.XPATH,'//img[@alt="vet-pharma-store"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary/specialities/vet-pharma-store":
    print("vet-pharma-store Redirection --> Passed")

else:
    print("vet-pharma-store Redirection --> Failed")
driver.back()


#To open  OPD
driver.find_element(By.XPATH,'//img[@alt="opd"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary/specialities/opd":
    print("OPD Redirection --> Passed")

else:
    print("OPD Redirection --> Failed")
driver.back()



#To open  Nutraceuticals
driver.find_element(By.XPATH,'//img[@alt="nutraceuticals"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary/specialities/nutraceuticals":
    print("Nutraceuticals Redirection --> Passed")

else:
    print("Nutraceuticals Redirection --> Failed")
driver.back()


#To open  Grooming
driver.find_element(By.XPATH,'//img[@alt="grooming"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary/specialities/grooming":
    print("Grooming Redirection --> Passed")

else:
    print("Grooming Redirection --> Failed")
driver.back()


#To open  Pet-shop
driver.find_element(By.XPATH,'//img[@alt="pet-shop"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary/specialities/pet-shop":
    print("Pet-shop Redirection --> Passed")

else:
    print("Pet-shop Redirection --> Failed")
driver.back()



#To open  soft-surgery
driver.find_element(By.XPATH,'//img[@alt="soft-surgery"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/veterinary/specialities/soft-surgery":
    print("soft-surgery Redirection --> Passed")
    print("Vet categories redirection --> Passed")

else:
    print("soft-surgery Redirection --> Failed")
driver.back()


# Go to Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()


#To open  Lab and Diagnostics
driver.find_element(By.XPATH,'//img[@alt="diagnostics"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics":
    print("Lab and Diagnostics Redirection --> Passed")

else:
    print("Lab and Diagnostics Redirection --> Failed")



#To open  Instrument
driver.find_element(By.XPATH,'//img[@alt="instrument"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics/categories/instrument":
    print("Instrument Redirection --> Passed")


else:
    print("Instrument Redirection --> Failed")
driver.back()


#To open  Biochemistry
driver.find_element(By.XPATH,'//img[@alt="biochemistry"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics/specialities/biochemistry":
    print("Biochemistry Redirection --> Passed")

else:
    print("Biochemistry Redirection --> Failed")
driver.back()


#To open  Rapid-card
driver.find_element(By.XPATH,'//img[@alt="rapid-card"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics/categories/rapid-card":
    print("Rapid-card Redirection --> Passed")

else:
    print("Rapid-card Redirection --> Failed")
driver.back()


#To open  Phlebotomy
driver.find_element(By.XPATH,'//img[@alt="phlebotomy"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics/specialities/phlebotomy":
    print("Phlebotomy Redirection --> Passed")

else:
    print("Phlebotomy Redirection --> Failed")
driver.back()


#To open  Diagnostic-test-kit
driver.find_element(By.XPATH,'//img[@alt="diagnostic-test-kit"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics/categories/diagnostic-test-kit":
    print("Diagnostic-test-kit Redirection --> Passed")

else:
    print("Diagnostic-test-kit Redirection --> Failed")
driver.back()


#To open  Equipment-accessories
driver.find_element(By.XPATH,'//img[@alt="equipment-accessories"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics/categories/equipment-accessories":
    print("Equipment-accessories Redirection --> Passed")

else:
    print("Equipment-accessories Redirection --> Failed")
driver.back()


#To open  Serology
driver.find_element(By.XPATH,'//img[@alt="serology"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics/specialities/serology":
    print("Serology Redirection --> Passed")

else:
    print("Serology Redirection --> Failed")
driver.back()



#To open  Poct
driver.find_element(By.XPATH,'//img[@alt="poct"]').click()


current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/diagnostics/specialities/poct":
    print("Poct Redirection --> Passed")
    print("Diagnostics categories redirections --> Passed")

else:
    print("Poct Redirection --> Failed")
driver.back()


# Go to Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()


#To open  Medicalequipments
driver.find_element(By.XPATH,'//img[@alt="medicalequipments"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments":
    print("Medicalequipments Redirection --> Passed")

else:
    print("Medicalequipments Redirection --> Failed")
driver.back()


#To open  Cardiology
driver.find_element(By.XPATH,'//img[@alt="cardiology"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments/specialities/cardiology":
    print("Cardiology Redirection --> Passed")

else:
    print("Cardiology Redirection --> Failed")
driver.back()

#To open  General-Surgery
driver.find_element(By.XPATH,'//img[@alt="general-surgery"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments/specialities/general-surgery":
    print("General-Surgery Redirection --> Passed")

else:
    print("General-Surgery Redirection --> Failed")
driver.back()


#To open  Dermatology
driver.find_element(By.XPATH,'//img[@alt="dermatology"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments/specialities/dermatology":
    print("Dermatology Redirection --> Passed")

else:
    print("Dermatology Redirection --> Failed")
driver.back()

#To open  Gynecology-Obstetrics
driver.find_element(By.XPATH,'//img[@alt="gynecology-obstetrics"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments/specialities/gynecology-obstetrics":
    print("Gynecology-Obstetrics Redirection --> Passed")

else:
    print("Gynecology-Obstetrics Redirection --> Failed")
driver.back()

#To open  Respiratory
driver.find_element(By.XPATH,'//img[@alt="respiratory"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments/specialities/respiratory":
    print("Respiratory Redirection --> Passed")

else:
    print("Respiratory Redirection --> Failed")
driver.back()

#To open  Hospital-Utilities
driver.find_element(By.XPATH,'//img[@alt="hospital-utilities"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments/specialities/hospital-utilities":
    print("Hospital-Utilities Redirection --> Passed")

else:
    print("Hospital-Utilities Redirection --> Failed")
driver.back()


#To open  Ophthalmology
driver.find_element(By.XPATH,'//img[@alt="ophthalmology"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments/specialities/ophthalmology":
    print("Ophthalmology Redirection --> Passed")

else:
    print("Ophthalmology Redirection --> Failed")
driver.back()


#To open  Diagnostics
driver.find_element(By.XPATH,'//img[@alt="diagnostics"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments/specialities/diagnostics":
    print("Diagnostics Redirection --> Passed")
    print("Medical Equipments Categories Redirection --> Passed")

else:
    print("Diagnostics Redirection --> Failed")
driver.back()



# Go to Homepage
driver.find_element(By.XPATH,"//img[contains(@class, 'sm:w-44')]").click()



#To open  Ophthalmology
driver.find_element(By.XPATH,'//img[@alt="ophthalmology"]').click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/medicalequipments/specialities/ophthalmology":
    print("Ophthalmology Redirection --> Passed")

else:
    print("Ophthalmology Redirection --> Failed")
driver.back()

#To open  Nexage Page
driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/a[1]/div[2]").click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/products?collection_slug=nex-gen-trendy-scrubs":
    print("Nexage Medical Wear Redirection --> Passed")

else:
    print("Nexage Medical Wear Redirection --> Failed")
driver.back()


#To open  Top Offers
driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[7]/a[1]/div[1]/img[1]").click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/products?collection_slug=top-offers":
    print("Top Offers Redirection --> Passed")

else:
    print("Top Offers Redirection --> Failed")
driver.back()

#To open  Hot Selling
driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/a[1]/div[1]/img[1]").click()

current_url = driver.current_url

if current_url == "https://www.medikabazaar.com/products?collection_slug=hot-selling":
    print("Hot Selling Redirection --> Passed")

else:
    print("Hot Selling Redirection --> Failed")
driver.back()

