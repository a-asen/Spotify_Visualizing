# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:46:58 2023

@author: steff
"""
#%% 
import os
import json
import pandas as pd

os.chdir("D:/coding/GitHub/a-asen/spotify_project") # Change working directory: Laptop 
os.chdir("D:/coding/GitHub/a-asen/spotify_project") # Change working directory: Home

#%%
#access_token  

#%%
os.path.exists("access")
print(os.getcwd())


#%%    Get access token
with open("access/access_token.json", "r") as f:
    access_token = json.load(f)
    
test = pd.read_json("access/access_token.json")

client = access_token["Client_ID"]
secret = access_token["Client"]



#%%
endpoint = "https://api.spotify.com"


import requests

url = "https://api.spotify.com/v1/me"

headers = {
    "Authorization": "<your_access_token>",
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)

print(response.json())

#%%%
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = client,
                                                           client_secret = secret))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])












