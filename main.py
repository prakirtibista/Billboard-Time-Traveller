import requests
from bs4 import BeautifulSoup
import datetime as dt
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import random
from pprint import pprint
load_dotenv()

url=os.environ.get('URL')
#input from user
date=input("Which year do you want to travel back to?YYYY-MM-DD: ")
year = int(date.split('-')[0])
#scraping the web
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
song_name=[]
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}",headers=headers)
soup = BeautifulSoup(response.text,'html.parser')
title = soup.select("li ul li h3")
for text in title:
    song_name.append(text.getText().strip())

scope="playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               client_id=os.environ.get('CLIENT_ID'),
                                               client_secret=os.environ.get("CLIENT_SECRET"), 
                                               redirect_uri=os.environ.get('REDIRECT_URL'),
                                               cache_path='token.txt',
                                               show_dialog= True,
                                               ))
cur_user = sp.current_user()

uri =[]
print("Creating your playlist....")
for song in song_name:
    search = sp.search(q=f"track:{song} year:{year}",type='track')
    
    try:
        uri.append(search['tracks']['items'][0]['uri'])
    except IndexError:
        print("Song not available")

playlist = sp.user_playlist_create(user = cur_user["id"],name=f"{date} Top 100",public=False)
#print(playlist)

add_songs = sp.playlist_add_items(playlist_id = playlist["id"],items=uri)
print("Enjoy Your Playlist 🤗")