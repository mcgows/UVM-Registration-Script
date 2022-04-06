import config
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

### Initialize the WebDriver
driver = webdriver.Safari()
driver.maximize_window()

### Go to the desired Starting Address
driver.get(config.URL)

### Automate Login
username_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "UserID"))
        )
username_box.send_keys(config.NETID)

password_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "PIN"))
        )
password_box.send_keys(config.NETID_PASSWORD + Keys.RETURN)

#### Select 'Registration'
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Registration"))
        )
element.click()

#### Select 'Register for Courses'
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Register/Add/Drop/Withdraw Classes"))
        )
element.click()

### Check registration term
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "term_id"))
        )
select = Select(element)

### Select option meeting current reg request
for o in select.options:
    if o.text is config.TERM:
        o.click()

### Submit the term request
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
element.click()

### Select all the ID Boxes
crn_boxes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[id^=crn_id"))
)

### Pass all CRNs to the Boxes
for index, crn in enumerate(config.CRNS):
    crn_boxes[index].send_keys(crn)
    if (index == len(config.CRNS) - 1) and config.SUBMIT:
        crn_boxes[index].send_keys(Keys.RETURN)

### Quit the Webdriver after defined time in the config file
if config.QUIT_AFTER > 0:
    time.sleep(config.QUIT_AFTER)
    driver.quit()