# -*- coding: utf-8 -*-
"""


### To-do ###
- [x] make culminative time ! so we can see whe nin the song we are lookin at 


- [ ] Remixed songs do not have a tag for "remixed", they are all 


"""
# %% set directory
if os.path.exists("D:/coding/GitHub/a-asen/spotify_project"):  # School
    path = "D:/coding/GitHub/a-asen/spotify_project"
if os.path.exists("D:/_coding/GitHub/a-asen/spotify_project"):  # Home
    path = "D:/_coding/GitHub/a-asen/spotify_project"

os.chdir(path)  # change directory
print(os.getcwd())  # get change


# %% packages
import os
import json
import pandas as pd
import spotipy
import matplotlib.pyplot as plt
import numpy as np
import lib.spotify_to_df as lib #local library
    # lib.top_tracks_df(sp) 
    # https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file


# %%  Read Keys
with open("access/access_token.json", "r") as f: # Get client ID and secret
    access_token = json.load(f)

# Redirect link:
sp_redirect = "http://localhost:8888/callback"
# Scopes (things we want to access - the "scope of our acccess")
sp_scopes = "user-read-playback-state,user-read-currently-playing,user-read-playback-position,user-top-read,user-read-recently-played,playlist-read-private,playlist-read-collaborative"

# https://developer.spotify.com/documentation/general/guides/authorization/scopes/
# https://spotipy.readthedocs.io/en/2.22.1/#spotipy.oauth2.SpotifyOAuth.__init__

# %%   Spotify Authentication
# https://spotipy.readthedocs.io/en/2.22.1/#spotipy.oauth2.SpotifyOAuth.__init__
sp_user_auth = spotipy.SpotifyOAuth(
    client_id       =  access_token["Client_ID"],     # client ID
    client_secret   =  access_token["Client_Secret"], # Secret
    redirect_uri    =  sp_redirect,                   # redirect to....
    scope           =  sp_scopes)                     # access scope

#sp_user_auth.get_auth_response()

# %%  Set the "auth_manager" to our credentials according to the given "auth" access
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
# We set our access point to "sp" by authorizing with "sp_user_auth"

sp = spotipy.Spotify(auth_manager = sp_user_auth)

#sp_user_auth.get_auth_response()
#sp_user_auth.get_authorization_code()

# %%   Top tracks
def top_tracks_df(limit: int = 50, time_range = str):
    """
    Get users top tracks.
     - Input:  Amount of top tracks
     - Output: Pandas dataframe
     
    # Example:
    top_tracks = user_top_tracks_df()
    """
    
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range = time_range)
    dl_top = []
    for item in top_tracks["items"]:
        d = {}
        d["track_title"] = item["name"]
        da = []
        for artist in item["artists"]:
            da.append(artist["name"])
        d["artists"] = da
        d["popularity"] = item["popularity"]
        d["uri"] = item["uri"]
        d["duration"] = item["duration_ms"]
        dl_top.append(d)
    return(pd.DataFrame(dl_top))

#%%
def track_analysis_to_df(audio_uri_list: list):
    """
    Do an audio analysis of a list of songs (ID, URI, URL)
     - Input:  List of song (ID, URI or URL)
     - Output: Pandas dataframe
     
    # Example:
    track_analysis = track_analysis_to_df(<my_top_tracks["uri"]>)
    """
    
    data_list = []  # where we put our informatio
    for enu, song in enumerate(audio_uri_list):  # For each
        analysis = sp.audio_analysis(song)
        for enu2, item in enumerate(analysis["segments"]):
            d = {}
            d["song index"]     = enu
            d["track index"]    = enu2
            d["time"]           = item["duration"]
            d["loudness_time"]  = item["loudness_max_time"]
            d["loudness_max"]   = item["loudness_max"]
           # d["loudness_end"]    =  item["loudness_end"] # doesnt add anything apparently
            d["pitch-1"]        = item["pitches"][0]
            d["pitch-2"]        = item["pitches"][1]
            d["pitch-3"]        = item["pitches"][2]
            d["pitch-4"]        = item["pitches"][3]
            d["pitch-5"]        = item["pitches"][4]
            d["pitch-6"]        = item["pitches"][5]
            d["pitch-7"]        = item["pitches"][6]
            d["pitch-8"]        = item["pitches"][7]
            d["pitch-9"]        = item["pitches"][8]
            d["pitch-10"]       = item["pitches"][9]
            d["pitch-11"]       = item["pitches"][10]
            d["pitch-12"]       = item["pitches"][11]
            d["timbre-1"]       = item["timbre"][0]
            d["timbre-2"]       = item["timbre"][1]
            d["timbre-3"]       = item["timbre"][2]
            d["timbre-4"]       = item["timbre"][3]
            d["timbre-5"]       = item["timbre"][4]
            d["timbre-6"]       = item["timbre"][5]
            d["timbre-7"]       = item["timbre"][6]
            d["timbre-8"]       = item["timbre"][7]
            d["timbre-9"]       = item["timbre"][8]
            d["timbre-10"]      = item["timbre"][9]
            d["timbre-11"]      = item["timbre"][10]
            d["timbre-12"]      = item["timbre"][11]
            data_list.append(d) # append this songs features to the list 
    return(pd.DataFrame(data_list))


# %%  Read  //  Get data

# NO NEED TO LOAD THE API UNNECESSARIY
# Check if we have stored the data
# Else get and save the data 

###############################################################################
##########                WORLD TOP TRACKS 2022!                  #############
### world top tracks 2022 (wtt22)
# only come with top 50 tracks
if os.path.exists("data/top_tracks_world_2022.csv"):
    wtt22 = pd.read_csv("data/top_tracks_world_2022.csv", index_col = 0) # Get col index. More pleasing to work with 
else:
    wtt22 = lib.playlist_to_df(sp, "37i9dQZF1DX18jTM2l2fJY")
    wtt22 = wtt22.set_index(wtt22.index + 1)      # set new index
    wtt22.to_csv("data/top_tracks_world_2022.csv")

############            World top tracks 2022 FEATURES           ##############
if os.path.exists("data/top_tracks_world_2022_features.csv"):
    wtt22f = pd.read_csv("data/top_tracks_world_2022_features.csv", index_col = 0)
else:
    wtt22f = sp.audio_features(wtt22["uri"])
    wtt22f = pd.DataFrame(wtt22f)
    wtt22f = wtt22f.drop(["id","track_href", "analysis_url","type"], axis = 1) # drop useless columns
    wtt22f = wtt22f.set_index(wtt22f.index + 1)
    wtt22f.to_csv("data/top_tracks_world_2022_features.csv")


###############################################################################
########                My Top Tracks 2022 (mtt22)                 ########## 
# 
if os.path.exists("data/my_top_tracks_2022.csv"):
    mtt22 = pd.read_csv("data/my_top_tracks_2022.csv", index_col = 0)
else:
    mtt22 = lib.playlist_to_df(sp, "37i9dQZF1F0sijgNaJdgit")
    mtt22 = mtt22.set_index(mtt22.index + 1)      # set new index
    mtt22.to_csv("data/my_top_tracks_2022.csv")

########             My Top Tracks 2022 Features (mtt22f)            ##########
if os.path.exists("data/my_top_tracks_2022_features.csv"):
    mtt22f = pd.read_csv("data/my_top_tracks_2022_features.csv", index_col = 0)
else:
    mtt22f = sp.audio_features(mtt22["uri"])
    mtt22f = pd.DataFrame(mtt22f)
    mtt22f = mtt22f.drop(["id","track_href", "analysis_url","type"], axis = 1) # drop useless columns
    mtt22f = mtt22f.set_index(mtt22f.index + 1)
    mtt22f.to_csv("data/my_top_tracks_2022_features.csv")


#%%    
###############################################################################
####                            Graphs                                     ####
###############################################################################
"""
# double plotting in matplotlib: https://matplotlib.org/stable/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py
# https://stackoverflow.com/a/8228808
 - plt.cla() clears an axis, i.e. the currently active axis in the current figure. It leaves the other axes untouched.
 - plt.clf() clears the entire current figure with all its axes, but leaves the window opened, such that it may be reused for other plots.
 - plt.close() closes a window, which will be the current window, if not specified otherwise.

# Thus we can make ONE FIGURE, ADD TO IT (ax) and clear it! 

Why am i missing help information on "ax" variable:
    lookup: https://matplotlib.org/stable/api/axes_api.html#basic
# to interpret features of track analysis: 
# https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features

# compare my music features to top 50 of norway ?
# https://open.spotify.com/playlist/37i9dQZEVXbJvfa0Yxg7E7?si=94da68a1315a418f
"""
#%% data shorthand 

dp = mtt22f.iloc[0:20,]
dp2 = wtt22f.iloc[0:20,]

#%% Quick figure of differences
fig, ax = plt.subplots()

# DATA PLOTTING
#  https://www.color-hex.com/color/00a170
plt.cla()
ax.plot(dp.index, dp["danceability"], c ="#32b38c", linewidth = 3)
ax.plot(dp2.index, dp2["danceability"], c ="#008059", linewidth = 2, linestyle = "dotted")

####   AX CHANGES
ax.back
ax.grid()
ax.set_yticks(np.arange(0.3,1.1,0.1))
xtick = np.arange(1,21,1).tolist()
# xtick.insert(0,1)
ax.set_xticks(xtick)
plt.ylim(0.35,1.05) # https://www.geeksforgeeks.org/matplotlib-pyplot-ylim-in-python/
plt.xlim(0.5,20.5)  # but why plt and not ax/fig?

# INFO
fig.legend(loc = "right", labels = ["World Top 20", "My Top 20"])
ax.set_title("Danceability", size = 16)


# ax.legend adds inside the AXES (the plot)
# ax.legend(labels = ["World Top 50", "My Top 50"], loc = "outside upper right")

# mean line?  Not that interesting ? 
ax.hlines(np.mean(dp["danceability"]), 1,50) 
ax.hlines(np.mean(dp2["danceability"]), 1,50)




# speechiness
ax.plot(dp.index, dp["speechiness"], c = "blue")

# energy
ax.plot(dp.index, dp["energy"], c ="yellow", linewidth = 3)

# valence
ax.plot(dp.index, dp["valence"], c ="black", linewidth = 3)
ax.plot(dp2.index, dp2["valence"], c ="black", linewidth = 3, linestyle = "dotted")

#useless
ax.plot(dp.index, dp["instrumentalness"], c ="red", linewidth = 3)
ax.plot(dp.index, dp["acousticness"], c ="purple", linewidth = 3)



#%%  BOXPLOT
fig2, ax2 = plt.subplots()

ax2.boxplot([dp["danceability"],
             dp2["danceability"],
             dp["valence"], 
            dp2["valence"]])
ax.title("")

#%% HIST 
dp = mtt22f.iloc[0:50]
dp2 = wtt22f.iloc[0:50]

fig3, ax3 = plt.subplots()
plt.cla()
ax3.hist(dp["danceability"], alpha = 0.4, color = "#4dac26")
ax3.hist(dp2["danceability"], alpha = 0.4, color = "#d0278b")
    


ax3.bar( height = dp["danceability"], alpha = 0.7, color = "blue")
plt.hist(dp["energy"],)
plt.hist(dp2["energy"])
#%% VERTICAL PLOT
fig2, (ax1, ax2) = plt.subplots(1,2) # to vertical


ax1.plot(dp.index, dp["danceability"])
# Using "dp" (data_plotting) to be able to quickly change data input in graph 
 
plt.cla()
# set background colour 
ax.set_facecolor("#e0e0e0")
ax.grid()
ax.set_xticks(np.arange(0.0,1.1,0.1))
ax.set_xtitle()
ax.set_yticks(np.arange(0.0,1.1,0.1))





ax.fill_between(dp.index, dp["danceability"], dp["speechiness"])
ax.fill_between(dp.index, dp["speechiness"])
ax.fill_between(dp.index, dp["danceability"],.9)

#ax.plot(msgf.index, msgf["tempo"], c ="purple", linewidth = 3)

ax.plot(dp.index, dp["loudness"], linewidth = 3)
ax.plot(msgf_10.index, np.log10(abs(msgf_10["loudness"])), linewidth = 3)
ax.set_xticks(np.arange(1,51,1))


ax.plot(msgf_10.index, msgf_10["danceability"])


plt.cla()




# %%  IF I WANT, I can do more "fine grane analysis of a specific track:
special = track_analysis_to_df(["5QdATOQJp1kififgPZYQ2Q"])

sp.audio_analysis("5QdATOQJp1kififgPZYQ2Q")
# ANALYSIS OF: 5QdATOQJp1kififgPZYQ2Q

# add loudness - do something fancy here
ax.plot(mtsf["culminative_time"], mtsf["loudness_max"])


ax.set_yticks(np.arange(-60,0,5))
ax.set_title("Loudness over time units")
ax.set_ylabel("Loudness")
ax.set_title("")
ax
plt.cla()

fig

ax.plot(mtsf["culminative_time"], mtsf["timbre-2"]) # add timbre 2
ax.plot(mtsf["culminative_time"], mtsf["timbre-3"]) # add timbre 3


# pitch to plot 
ax.plot(mtsf["culminative_time"], mtsf["pitch-1"]) # add

# log transform to fit pitch in plot: 
# https://www.geeksforgeeks.org/log-and-natural-logarithmic-value-of-a-column-in-pandas-python/
np.log(mtsf.loc[:,"timbre-1":"timbre-12"])
np.log(mtsf.loc[:,"timbre-2"])


# grand mean over pitch
# https://statisticsglobe.com/calculate-mean-python
ax.plot(mtsf["culminative_time"], mtsf.loc[:,"timbre-1":"timbre-12"].mean(axis=1))




# SET OTHER INFORMATION TO "AX"
# ax.set_yticks(np.arange(-200,100,20))







