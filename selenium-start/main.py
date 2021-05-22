from selenium import webdriver

chrome_driver_path = "/home/larisa/dev/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.de/-/en/dp/B08PCCCZQ7/ref=sr_1_fkmr1_1?crid=1V71IA2O81AJM&dchild=1&keywords=iphone%2B12%2Bpro%2Bmax%2B516%2Bgb&qid=1621505646&sprefix=iphone%2Bpro%2B516%2Caps%2C196&sr=8-1-fkmr1&th=1")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

driver.get("https://python.org/")

# search_bar = driver.find_element_by_name("q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)
# bug_link = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[4]/h2')
# print(bug_link.text)
elements = driver.find_elements_by_css_selector(".event-widget li")
res = {}
for i, el in enumerate(elements):
    time = el.find_element_by_css_selector("time").get_attribute("textContent")
    event = el.find_element_by_css_selector("a").get_attribute("textContent")
    res[i] = {"time": time, "name": event}
   
    # print(el.get_attribute("textContent"))
# driver.close()
print(res)
driver.quit()