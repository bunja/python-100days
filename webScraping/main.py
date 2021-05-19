from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_upvotes)
# print(article_links)
# print(article_texts)

# max = 0

# for index in range(len(article_upvotes)):
#     if article_upvotes[index] >= max:
#         max = article_upvotes[index]
#         i_max = index

# print(max, i_max)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(largest_index)
print(article_texts[largest_index])


# with open("website.html") as file:
#     contens = file.read()

# soup = BeautifulSoup(contens, "html.parser")
# # print(soup.pretify)

# # all_a_tags = soup.find_all(name="a")
# # print(all_a_tags)

# # for tag in all_a_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))