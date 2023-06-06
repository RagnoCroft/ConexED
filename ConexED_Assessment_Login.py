import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Generate a random email address
def generate_random_email():
    random_part = ''.join(random.choices(string.digits, k=8))
    email = f"olverajc+{random_part}@gmail.com"
    return email

# 1. Navigates to https://my.test.craniumcafe.com/
chrome_driver_path='/Program Files (x86)/Google/ChromeDriver'
driver = webdriver.Chrome()
driver.get("https://my.test.craniumcafe.com/")

# 2. Searches for and selects 'Cranium Cafe - Test' and waits until the search results are loaded
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID,'school-search')))
search_box = driver.find_element(By.ID,'school-search')
search_box.send_keys("Cranium Cafe - Test")
search_box.send_keys(Keys.ENTER)

# Waits for the 'Cranium Cafe - Test's login' modal to open
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID,'integration-redirect-button')))
cafe_link = driver.find_element(By.ID,'integration-redirect-button')
cafe_link.click()

# Wait for the new window or tab to open
wait = WebDriverWait(driver, 10)
wait.until(EC.number_of_windows_to_be(2))

# Switch to the newly opened window or tab
driver.switch_to.window(driver.window_handles[1])

# 3. Clicks 'Guest Registration' and completes the registration
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.ID,'login-iframe')))
login_iframe = driver.find_element(By.ID,'login-iframe')
driver.switch_to.frame(login_iframe)

wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.ID,'craniumcafe-button')))
test_button = driver.find_element(By.ID,'craniumcafe-button')
test_button.click()

# No Account? Register Here!
register_here_button = driver.find_element(By.ID,'register-toggle-button')
register_here_button.click()

# Fill in the registration form with the required details
name_input = wait.until(EC.presence_of_element_located((By.ID, "fullname-text")))
name_input.send_keys("John Doe")

random_email = generate_random_email()
email_input = driver.find_element(By.ID,"email-text")
email_input.send_keys(random_email)

password_input = driver.find_element(By.ID,"create-password-text")
password_input.send_keys("Pa55word!")

confirm_password_input = driver.find_element(By.ID,"confirm-password-text")
confirm_password_input.send_keys("Pa55word!")

register_button = driver.find_element(By.ID,"register-button")
register_button.click()

#From here on, all code is commented until Line 134. I have decided to leave the Gmail login as a hypothetical scenario which is why I commented the whole scenario.
#I have faced some complications which I list below.
# I. All the testing I commited was done on my personal gmail account, which require me to explicitly hard-code in my credentials. I kindly prefer not to do so.
# II. A workaround could be to create a ConexED Gmail account and use it instead. I didn't do that and instead I left all the code as a hypothetical scenario.
# III. Selenium WebDriver appears to be blocked by Google starting at some point on or after 2019 and currently there appears to be no workaround.
# IV. The code below would work on my personal gmail account if it wasn't for Google's new security policy.
# V. Another workaround could be the use of a third-party sandbox account which at that point it can be recoded accordingly.

########Open Gmail and wait for it to open.
#######driver.get('https://www.gmail.com')
########wait = WebDriverWait(driver, 10)
########wait.until(EC.number_of_windows_to_be(3))

######## Find and fill in the email field
#######email_input = driver.find_element(By.ID, 'identifierId')
#######email_input.send_keys(random_email)

######## Click on the "Next" button
#######next_button = driver.find_element(By.ID, 'identifierNext')
#######next_button.click()

######## Wait until the password field is visible
#######password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'password')))

######## Fill in the password field
#######password_input.send_keys('Pa55word!')

######## Click on the "Next" button
#######password_next_button = driver.find_element(By.ID, 'passwordNext')
#######password_next_button.click()

######## Wait until the Gmail inbox is loaded
#######WebDriverWait(driver, 10).until(EC.title_contains('Inbox'))

######## Search for ConexED email
#######search_input = driver.find_element(By.XPATH, '//input[@aria-label="Search mail"]')
#######search_input.send_keys('Welcome to Your ConexED Account!')

######## Press Enter to perform the search
#######search_input.send_keys(Keys.ENTER)

######## Wait until the search results are loaded
#######WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@role="main"]//div[@role="checkbox"]')))

######## Find and click on the specific email
#######email_link = driver.find_element(By.XPATH, '//span[contains(text(), "Welcome to Your ConexED Account!")]')
#######email_link.click()

######## Wait until the email is loaded
#######WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@role="dialog"]//div[@dir="ltr"]')))

######## Get the contents of the email
#######email_contents = driver.find_element(By.XPATH, '//div[@role="dialog"]//div[@dir="ltr"]').text

######## Find the specific hyperlink and click on it
#######hyperlink_text = 'https://cc.test.craniumcafe.com/register/'
#######hyperlink_element = driver.find_element(By.XPATH, f'//a[contains(text(), "{hyperlink_text}")]')
#######hyperlink_element.click()

driver.quit()

# 4. Once registered, use the same login credentials to log in
driver = webdriver.Chrome()
driver.get("https://my.test.craniumcafe.com/")

# Searches for and selects 'Cranium Cafe - Test' and waits until the search results are loaded
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID,'school-search')))
search_box = driver.find_element(By.ID,'school-search')
search_box.send_keys("Cranium Cafe - Test")
search_box.send_keys(Keys.ENTER)

#Click on 'Take me there!' again.
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID,'integration-redirect-button')))
cafe_link = driver.find_element(By.ID,'integration-redirect-button')
cafe_link.click()

# Wait for the new window or tab to open
wait = WebDriverWait(driver, 10)
wait.until(EC.number_of_windows_to_be(2))

# Switch to the newly opened window or tab
driver.switch_to.window(driver.window_handles[1])

# Clicks 'Guest Registration' and proceeds to login for the first time!
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.ID,'login-iframe')))
login_iframe = driver.find_element(By.ID,'login-iframe')
driver.switch_to.frame(login_iframe)

wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.ID,'craniumcafe-button')))
test_button = driver.find_element(By.ID,'craniumcafe-button')
test_button.click()

login_email_input = wait.until(EC.presence_of_element_located((By.ID, "login-text")))
login_email_input.send_keys(random_email)
login_email_input.send_keys(Keys.TAB)

login_password_input = driver.find_element(By.ID,"password-text")
login_password_input.send_keys("Pa55word!")

login_button = driver.find_element(By.ID,"login-button")
login_button.click()

## Close the browser
driver.quit()

