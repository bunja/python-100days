from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

chrome_driver_path = "/home/larisa/dev/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(os.getenv("LINKEDIN_URL"))

sign_in_button = driver.find_element_by_class_name("nav__button-secondary")
sign_in_button.click()

username = driver.find_element_by_id("username")
username.send_keys(os.getenv("LINKEDIN_USERNAME"))
password = driver.find_element_by_id("password")
password.send_keys(os.getenv("LINKEDIN_PASSWORD"))
button = driver.find_element_by_css_selector("button.btn__primary--large.from__button--floating")
button.click()
jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in jobs:
    print("called")
    job.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_class_name("jobs-apply-button")
        apply_button.click()
    
        submit = driver.find_element_by_xpath("//*[text()='Submit application']")
        if submit.get_attribute("data-control-name") == "continue_unify":
            close = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close.click()
            discard = driver.find_element_by_xpath("//*[text()='Discard']")
            discard.click()
            print("complex application skipped")
            continue
        else:
            submit.click()
        
        close = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close.click()
        
    except NoSuchElementException:
        print("Oops No SUCH BUTTON")
        continue

time.sleep(5)
driver.quit()
        

    
