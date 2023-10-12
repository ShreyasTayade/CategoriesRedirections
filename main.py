from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch the web browser
browser = webdriver.Chrome()

# Navigate to the login page
browser.get('https://vet.medikabazaar.com/account/login')

browser.find_element_by_name('email').send_keys
# Locate the email and password input fields
email_field = browser.find_element_by_name('email')
password_field = browser.find_element_by_name('password')

# Input the email and password credentials
email_field.send_keys('your_email@example.com')
password_field.send_keys('your_password')

# Simulate clicking the login button
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Wait for the dashboard page to load
browser.implicitly_wait(10)

# Print the title of the dashboard page
print(browser.title)

# Close the browser
browser.quit()
