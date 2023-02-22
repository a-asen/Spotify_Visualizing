# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 12:46:58 2023

@author: steff
"""
#%% 
import os

os.chdir("D:/coding/GitHub/a-asen/spotify_project") # set wprlomg dorectpry
#%%
#access_token  

#%%
os.path.exists("access")
print(os.getcwd())

import json
#%%
with open("access/access_token.json", "r") as f:
    access_token = json.load(f)

client = access_token["Client_ID"]
secret = access_token["Client "]

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