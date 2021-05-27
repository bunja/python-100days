from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

chrome_driver_path = "/home/larisa/dev/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
INST_USERNAME = os.getenv("INST_USERNAME")
INST_PASS = os.getenv("INST_PASS")
SIMILAR_ACC = "chefsteps"

class InstaFollower():

    def __init__(self, driver):
        self.driver = driver
    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        accept_cookies_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]')
        accept_cookies_button.click()
        time.sleep(2)
        username = self.driver.find_element_by_name('username')
        username.send_keys(INST_USERNAME)
        password = self.driver.find_element_by_name('password')
        password.send_keys(INST_PASS)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login_button.click()
        time.sleep(3)
        save = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        save.click()
        time.sleep(2)
        not_now_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_button.click()



    def find_followers(self):
        self.driver.get('https://www.instagram.com/chefsteps/')
        followers_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_link.click()
        time.sleep(3)
        
        popup_window = self.driver.find_element_by_css_selector('div.isgrP')
        count = 10
        while count > 0:
            
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',  popup_window)
            time.sleep(1)

            count = count - 1



    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector('li button')
        # follow_buttons = popup_window.find_elements_by_xpath("//button[text()='Follow']")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower(driver)
bot.login()
bot.find_followers()
bot.follow()