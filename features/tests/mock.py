from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Create a new Chrome browser instance
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Open Target homepage
    driver.get('https://www.target.com/')
    driver.maximize_window()

    # Step 2: Click the 'Sign In' button
    sign_in_button = driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']")
    sign_in_button.click()

    # Continue with your code...

finally:
    # Close the browser
    driver.quit()
