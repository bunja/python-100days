import requests
from bs4 import BeautifulSoup

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://raw.githubusercontent.com/SadSack963/day-45_web_scraping/master/data/100_best_movies.html"

response = requests.get(URL)
website_html = response.text

# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

# for n in range(len(movie_titles) - 1, -1, -1):
#     print(movie_titles[n])

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")



