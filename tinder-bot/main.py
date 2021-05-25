from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

fb_usrname = os.getenv("FB_USERNAME")
fb_pass = os.getenv("FB_PASS")

chrome_driver_path = "/home/larisa/dev/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")

create_acc_button = driver.find_element_by_xpath("//*[text()='Create Account']")
create_acc_button.click()
time.sleep(3)
fb_button = driver.find_element_by_xpath("//button[@aria-label='Log in with Facebook']")
fb_button.click()

time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(5)
accept_all_button = driver.find_element_by_xpath("//button[@data-cookiebanner='accept_button']")
accept_all_button.click()

input_email = driver.find_element_by_id("email")
input_email.send_keys(fb_usrname)
input_pass = driver.find_element_by_id("pass")
input_pass.send_keys(fb_pass)
login_button = driver.find_element_by_name("login")
login_button.click()
time.sleep(3)
# confirm = driver.find_element_by_name("__CONFIRM__")
# confirm.click()
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(6)
location_allow = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[1]/span')
location_allow.click()
time.sleep(2)
notifications_dismiss = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[2]/span')
notifications_dismiss.click()
time.sleep(2)
cookies_accept = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[2]/div/div/div[1]/button')
cookies_accept.click()
number_of_likes = 10
while number_of_likes >= 0:
    time.sleep(2)
    try:
        like = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like.click()
        number_of_likes = number_of_likes - 1
    except NoSuchElementException:
        print("ops")
    except ElementClickInterceptedException:
        back_to_tinder = driver.find_elements_by_xpath("//button[@title='Back to Tinder']")
        if len(back_to_tinder) > 0:
            back_to_tinder[0].click()
        else:
            not_interested = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div[2]/button[2]')
            not_interested.click()
driver.quit()



