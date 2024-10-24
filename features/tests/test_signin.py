from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
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
    sleep(3)  # Give the page time to load

    # Step 2: Click the 'Sign In' button (main page)
    sign_in_button = driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']")
    sign_in_button.click()
    sleep(3)  # Wait for the side navigation to load

    # Step 3: Click 'Sign In' from the side navigation
    sign_in_from_nav = driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
    sign_in_from_nav.click()
    sleep(3)  # Wait for the Sign In page to load

    # Step 4: Verify that the Sign In page is displayed
    # Check for the "Sign into your Target account" text
    sign_in_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Sign into your Target account')]")
    print("Sign-In text is visible:", sign_in_text.is_displayed())

    # Check if Sign-In button is visible (on the actual Sign In form page)
    sign_in_button_check = driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
    print("Sign-In button is visible:", sign_in_button_check.is_displayed())

finally:
    # Close the browser
    driver.quit()
