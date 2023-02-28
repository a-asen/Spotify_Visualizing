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
#if os.path.exists("D:/_coding/GitHub/a-asen/spotify_project"): # Home
 #   path = "D:/_coding/GitHub/a-asen/spotify_project"
    
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

#%% Get user. 
my_user = sp.user_playlists("1117238547")

my_user.keys()
my_user["items"][1].keys()

my_user["items"][1]

#%%
for row in my_user["items"]:
    print(row["name"])
    print(row["id"])


#%%  
# Get my playlist 
my_playlist = sp.playlist("5QYCZkI9ecneIK5OjveBsE")  # 2023 - MixTape
# dat = json.dumps(my_playlist) # save to file

for enu, data in enumerate(my_playlist["tracks"]["items"]):
   
    print(enu)
   
    d = {} # New dictinary (to add playlist information)
    artist_list = [] # List to get out "multiple" artits
    
    # Track information
    d["number"]       = data["track"]["track_number"]    # Track number in the playlist 
    d["name"]         = data["track"]["name"]            # Name of the song
    
    for artist in data["track"]["artists"]:
        artist_list.append(artist["name"])
    d["aritsts"]      = artist_list
    d["artists"]      = data["track"]["artists"][""]
    d["popularity"]   = data["track"]["popularity"]      # How popular the song is
    d["duration"]     = data["track"]["duration_ms"]     # How long the song is 
    
    # Meta-data
    d["id"]           = data["track"]["id"]              # Id of the track 
    d["added_date"]   = data["added_at"]                 # The date at which the song was added to the playlist
    d["added_by"]     = data["added_by"]["id"]           # The person who added the song to the playlist
    data["track"]["is_local"]
    data["track"].keys()
    data["track"]["name"]
    data["track"]["name"]
    data["track"]["name"]
    

    print(data[enu]["track"])
    for y in x["track"]:
        y.keys()
    
    if "track" in x:
        print(x)
        for y in x["track"]:
            print(y)
            # print(y["uri"])
            # print(y["name"])


#%%%      ####### AUDIO FEATURE
audio_feature.keys()
audio_feature = sp.audio_analysis('spotify:track:0o3G5EAvMwjzqX5cH55Kw5')




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









