from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")
for job in jobs:
    # print(job.text)
    job.click()
    time.sleep(2)
    apply_button = driver.find_elements_by_class_name("jobs-apply-button")
    if len(apply_button) == 0:
        continue
    apply_button[0].click()
    time.sleep(0.5)

    submit_button = driver.find_element_by_css_selector(".artdeco-modal .jobs-easy-apply-content button.artdeco-button--primary")
    button_text = submit_button.text.strip().lower()

    if button_text != 'submit application':
        close = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close.click()
        discard = driver.find_element_by_xpath("//*[text()='Discard']")
        discard.click()
        print("complex application skipped")
        continue

    submit_button.click()

    time.sleep(0.5)

    close = driver.find_element_by_css_selector("button.artdeco-modal__dismiss")
    close.click()

    break
