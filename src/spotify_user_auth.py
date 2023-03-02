# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:49:54 2023

@author: steff
"""

##### User authorization to read private and history
# %% packages
import os
import json
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# %% set directory
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
sp_api_url = "https://api.spotify.com/v1" # we use this cause this is where "GET" responses come from

# https://developer.spotify.com/documentation/general/guides/authorization/scopes/

sp_scopes = "user-read-recently-played"  # Scopes
# [


sp_redirect = "http://localhost:8888/callback" # Local to grantk access? 
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize' # no idea? 
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'     # no idear 
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
 



["user-read-playback-state", "user-read-currently-playing", 
             "user-read-playback-position", "user-top-read", "user-read-recently-played"
             "playlist-read-private", "playlist-read-collaborative"]

# %%  Spotify accesss
#sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = sp_client,
 #                                                            client_secret = sp_secret))


# %%
test = spotipy.SpotifyOAuth(client_id     = sp_client,      # client ID
                            client_secret = sp_secret,  # Secret
                            redirect_uri  = sp_redirect,  # redirect to....
                            scope         = sp_scopes)             # access scope

abd = test.get_access_token()
test.

spotipy.oauth2.SpotifyOAuth()

spotipy.Spotify(auth=())

test.open_browser()
test.get_authorize_url()
test.get_auth_response()


spot_auth = spotipy.oauth2.SpotifyOAuth(client_id     = sp_client,      # client ID
                            client_secret = sp_secret,  # Secret
                            redirect_uri  = sp_redirect,  # redirect to....
                            scope         = sp_scopes)             # access scope
spot_auth.get_access_token()

# %%
sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = sp_client,
                                                             client_secret = sp_secret))

#
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(
    client_id      = sp_client,     # Spotify developer client ID 
    client_secret  = sp_secret,     # Spotify developer client secret
    #redirect_uri  = sp_api_url,    # redirect to spotify API call
    redirect_uri   = sp_redirect,   # testing local call? 
    scope          = sp_scopes))    # Scopes (a list should be OK)
# see -> https://spotipy.readthedocs.io/en/2.22.1/#spotipy.oauth2.SpotifyOAuth.__init__


user_recently_played = sp.current_user_recently_played()

user_recently_played["items"][0].keys()
user_recently_played["items"][0]["track"].keys()

user_recently_played["items"][0]["track"]["name"]



