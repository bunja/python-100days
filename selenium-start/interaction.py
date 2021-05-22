from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/larisa/dev/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# count = driver.find_element_by_css_selector("a[title='Special:Statistics']")
# # count.click()
# print(count.text)

# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element_by_name("fName")
fname.send_keys("lara")


lname = driver.find_element_by_name("lName")
lname.send_keys("klara")

email = driver.find_element_by_name("email")
email.send_keys("lara@klara.com")


submit = driver.find_element_by_css_selector("form button")
submit.click()



# driver.quit()
