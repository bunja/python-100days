import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("what year would you like to travel to? (YYYY-MM-DD)")
year = date.split("-")[0]

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
website_html = response.text

# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")

song_names_spans = soup.find_all(name="span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
# print(song_names)


CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
scope = "playlist-modify-public"
REDIRECT = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri=REDIRECT))

user_id = sp.current_user()["id"]
song_uris = []
for song in song_names:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    # print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        # print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify.Skipped")

billboard100 = sp.user_playlist_create(user_id, name=f"{date} Billboard 100")
print(billboard100)

playlist_id = billboard100['id']
print(playlist_id)

sp.playlist_add_items(playlist_id, song_uris, position=None)

