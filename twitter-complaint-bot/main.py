from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
chrome_driver_path = "/home/larisa/dev/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
TW_EMAIL = os.getenv("TW_EMAIL")
TW_PASS = os.getenv("TW_PASS")

class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.down = 0
        self.up = 0
        self.driver = driver

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        concent_button = driver.find_element_by_id("_evidon-banner-acceptbutton")
        concent_button.click()
        go_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(60)
        self.down = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        
        self.up = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]').text
        # driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(3)
        tw_login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/a[2]')
        time.sleep(2)
        tw_login_button.click()
        username = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(TW_EMAIL)
        password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TW_PASS)
        login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        login_button.click()
        time.sleep(3)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up "
        tw_input_field = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
        tw_input_field.send_keys(tweet)
        time.sleep(3)
        tweet_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_button.click()

bot = InternetSpeedTwitterBot(driver)
bot.get_internet_speed()

bot.tweet_at_provider()

