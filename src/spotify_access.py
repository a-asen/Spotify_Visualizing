# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:46:58 2023

@author: steff
"""
#%% 
import os
import json

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


if os.path.exists("D:/coding/GitHub/a-asen/spotify_project"): # School 
    path = "D:/coding/GitHub/a-asen/spotify_project"
if os.path.exists("D:/_coding/GitHub/a-asen/spotify_project"): # Home
    path = "D:/_coding/GitHub/a-asen/spotify_project"
    
os.chdir(path)
print(os.getcwd())

#%%  Read Keys
os.path.exists("access")

# Get access token # Read JSON
with open("access/access_token.json", "r") as f:
    access_token = json.load(f)

sp_client = access_token["Client_ID"]
sp_secret = access_token["Client_Secret"]

#%%%  Spotify accesss
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = sp_client,
                                                           client_secret = sp_secret))

#%% Read my user
my_user = sp.user_playlists("1117238547")

#%%  Read my playlist 
# Get my playlist 
my_playlist = sp.playlist("5QYCZkI9ecneIK5OjveBsE")  # 2023 - MixTape
# dat = json.dumps(my_playlist) # save to file

# Get "dict" keys
my_playlist.keys()
    # 'collaborative', 'description', 'external_urls', 'followers', 'href', 'id', 'images', 
    # 'name', 'owner', 'primary_color', 'public', 'snapshot_id', 'tracks', 'type', 'uri'
        # "tracks" most useful    # my_playlist["tracks"]

# Get "dict" keys under "tracks"
my_playlist["tracks"].keys()
    # 'href', 'items', 'limit', 'next', 'offset', 'previous', 'total'
        # "items" and "total" useful    # my_playlist["tracks"]["items"]

# Get dict keys under "items" under "tracks" 
    # my_playlist["tracks"]["items"].keys() 
    len(my_playlist["tracks"]["items"])

# Under "tracks","items" we have a list. Access respectively with "[0]" 
my_playlist["tracks"]["items"][0].keys()
    # 'added_at', 'added_by', 'is_local', 'primary_color', 'track', 'video_thumbnail'
    # "track" most useful 

# under "tracks" under any respective item under "items" under "tracks"
my_playlist["tracks"]["items"][0]["track"].keys()
    # 'album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'episode', 'explicit', 'external_ids', 
    # 'external_urls', 'href', 'id', 'is_local', 'name', 'popularity', 'preview_url', 'track', 'track_number', 'type', 'uri'


my_playlist["tracks"]["items"][0]["track"]["uri"]

my_playlist["tracks"]["items"][0]["track"]["track_number"]
my_playlist["tracks"]["items"][0]["track"]["name"]

my_playlist["tracks"]["items"][0]["track"]["popularity"]
my_playlist["tracks"]["items"][0]["track"]["duration_ms"]
my_playlist["tracks"]["items"][0]["track"]["track"]


my_playlist["tracks"]["items"]#[0]#["track"]
["name"]




for i in my_playlist["tracks"]["items"]:
    print(i)["name"]

my_playlist["tracks"]["items"]


my_playlist.items()

for x in my_user:
    print(x)
    print(my_user["href"][x])
    
my_user["href"]

with open("data/my_data.json","w") as f: 
    f.write(dat)

"""
for name, id0 in enumerate(my_user):
    print(name, id0)
"""






#%%%
"""

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


"""









