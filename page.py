from selenium import webdriver

# Create an instance of the webdriver for Chrome
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://vet.medikabazaar.com/")

# Find the search box and enter a search query
search_box = driver.find_element_by_name("search_text")
search_box.send_keys("your search query")

# Click the search button
search_button = driver.find_element_by_xpath("//button[@type='submit']")
search_button.click()

# Close the browser
driver.close()
