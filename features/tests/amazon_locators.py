from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

# Set up Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Create a new Chrome browser instance
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Step 1: Open Amazon Sign-In page
    driver.get('https://www.amazon.com/ap/signin')
    driver.maximize_window()
    sleep(3)  # Give the page time to load

    # Step 2: Locate the Amazon Logo
    amazon_logo = driver.find_element(By.XPATH, "//a[@href='/ref=ap_frn_logo']")
    print("Amazon Logo is visible:", amazon_logo.is_displayed())

    # Step 3: Locate the Email Field
    email_field = driver.find_element(By.CSS_SELECTOR, "#ap_email")
    print("Email Field is present:", email_field.is_displayed())

    # Step 4: Locate the Continue Button
    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
    print("Continue Button is present:", continue_button.is_displayed())

    # Step 5: Locate Conditions of Use Link
    conditions_of_use_link = driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")
    print("Conditions of Use Link is present:", conditions_of_use_link.is_displayed())

    # Step 6: Locate Privacy Notice Link
    privacy_notice_link = driver.find_element(By.XPATH, "//a[contains(@href, 'privacy_notice')]")
    print("Privacy Notice Link is present:", privacy_notice_link.is_displayed())

    # Step 7: Locate Need Help Link
    need_help_link = driver.find_element(By.XPATH, "//span[contains(text(), 'Need help?')]")
    print("Need Help Link is present:", need_help_link.is_displayed())

    # Step 8: Locate Forgot Your Password Link
    forgot_password_link = driver.find_element(By.CSS_SELECTOR, "#auth-fpp-link-bottom")
    print("Forgot Your Password Link is present:", forgot_password_link.is_displayed())

    # Step 9: Locate Other Issues with Sign-In Link
    other_issues_link = driver.find_element(By.CSS_SELECTOR, "#ap-other-signin-issues-link")
    print("Other Issues with Sign-In Link is present:", other_issues_link.is_displayed())

    # Step 10: Locate Create Your Amazon Account Button
    create_account_button = driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit")
    print("Create Your Amazon Account Button is present:", create_account_button.is_displayed())

finally:
    # Close the browser
    driver.quit()
