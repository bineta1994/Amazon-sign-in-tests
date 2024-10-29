# Amazon Logo
amazon_logo = driver.find_element(By.CSS_SELECTOR, "a.a-link-nav-icon")

# "Create account" Header
create_account_header = driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# "Your name" Input Field
your_name_field = driver.find_element(By.ID, "ap_customer_name")

# "Email" Input Field
email_field = driver.find_element(By.ID, "ap_email")

# "Password" Input Field
password_field = driver.find_element(By.ID, "ap_password")

# "Re-enter password" Input Field
reenter_password_field = driver.find_element(By.ID, "ap_password_check")

# "Create your Amazon account" Button
create_account_button = driver.find_element(By.ID, "continue")

# "Conditions of Use" Link
conditions_of_use_link = driver.find_element(By.LINK_TEXT, "Conditions of Use")

# "Privacy Notice" Link
privacy_notice_link = driver.find_element(By.LINK_TEXT, "Privacy Notice")

# "Sign in" Link
sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")