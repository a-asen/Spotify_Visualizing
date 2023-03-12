# -*- coding: utf-8 -*-
"""


### To-do ###
- [x] make culminative time ! so we can see whe nin the song we are lookin at 


- [ ] Remixed songs do not have a tag for "remixed", they are all 


"""
# %% packages
import os
import json
import pandas as pd
import spotipy
import seaborn as sb

# Alternatively, a local "package" of functions can be achieved through this:
# import lib.spotify_to_df as sp_df
# sp_df.top_tracks_df(sp, 10)
# https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file


# %% set directory
if os.path.exists("D:/coding/GitHub/a-asen/spotify_project"):  # School
    path = "D:/coding/GitHub/a-asen/spotify_project"
if os.path.exists("D:/_coding/GitHub/a-asen/spotify_project"):  # Home
    path = "D:/_coding/GitHub/a-asen/spotify_project"

os.chdir(path)  # change directory
print(os.getcwd())  # get change

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

"""
PROBLEM WITH TOKEN AFTER PASSWORD RESET: 
    In my case the token had not expired, but was changed (probably because of 
    a forced password change by spotify), which led to "wrongful calls".
    Spotipy was not able to resolve this issue automatically. 
  SOLUTION:
      Manually deleting the ".cache" file solved this issue by refreshing the
      token 
    
# Spotipy is supposed to do the following:
# 1. Check ".cache" file (or ".cache-<username>")
# 2. If its expired -> refresh it
# 3. If not in ".cache" open browser and store it in ".cache"
# https://stackoverflow.com/questions/48883731/refresh-token-spotipy

### My own thoughts
I suppose this (redirect_uri) is where the data is being sent to, where
we access the data?  Therefore it is also a "local" target.
We might, I guess, put up a server target (https://cross_sync.com:8080/callback)
to handle responses to certain server? apps.
redirect_uri  = sp_api_url # redirect to spotify API call
Does not work with this code, hence the above
"""

# %%  Set the "auth_manager" to our credentials according to the given "auth" access
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
# We set our access point to "sp" by authorizing with "sp_user_auth"

sp = spotipy.Spotify(auth_manager = sp_user_auth)

# %%   Top tracks
def top_tracks_df(limit: int = 50):
    """
    Get users top tracks.
     - Input:  Amount of top tracks
     - Output: Pandas dataframe
     
    # Example:
    top_tracks = user_top_tracks_df()
    """
    
    top_tracks = sp.current_user_top_tracks(limit=limit)
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

# %%  Get song analysis
def track_analysis_to_df(audio_uri_list: str):
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

#%%
def track_analysis_to_df(audio_uri_list: str):
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
if os.path.exists("data/my_top_50.csv"): # check if we already have data 
    # no need to load the api unecessarily
    # mtt = my_top_tracks
    mtt = pd.read_csv("data/my_top_50.csv")
else: # if not, we get the data and save it
    mtt = top_tracks_df() # get my top 50 songs (so far: 2023.03.11)    
    mtt.to_csv("data/my_top_50.csv", index = False) # save it 
    
if os.path.exists("data/my_top_50_analysis.csv"):
    # mtta== my_top_tracks_analysis
    mtta = pd.read_csv("data/my_top_50_analysis.csv")
else:
    mtta = track_analysis_to_df(mtt["uri"]) # get features
    mtta["culminative_time"] = pd.NA # new var
    for value in mtta.index:
        if mtta["track index"][value] == 0: # if we start a new track we start from this "time" value
            mtta["culminative_time"][value] = mtta["time"][value]
                    
            mtta.loc[value,"culminative_time"]
        elif mtta["track index"][value] > 0: # if we are on the same track, we continue from last value 
            mtta["culminative_time"][value] = mtta["culminative_time"][value-1] + mtta["time"][value]
            
    mtta.to_csv("data/my_top_50_analysis.csv", index = False)


# %% Subset
# get out my favorite song features
# mtsf = my_top_song_features
mtsf = mtta[mtta["song index"] == 0] # subset of my top song.



##### MAYBE NOT, BELOW
# %%  Pivot dataframe for seaborn graph:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.wide_to_long.html
mtsf_long = pd.wide_to_long(mtsf,
                            #we want togather  timbre and pitch to one variable
                            stubnames = ["timbre", "pitch"],  
                            sep = "-", # get all timbre based on a "-" split ("timbre-"1 /// timbre-"2)
                            i = "track index",  # based on track index
                            j = "value_index")  # give it a new variable "track_index"

mtsf_long = mtsf_long.reset_index() # add our indexs to the dataframe 

# double seaborn (based on columns?):  https://seaborn.pydata.org/tutorial/relational.html
    # require pivot? 

# %%   Seaborn data selection 
# https://stackoverflow.com/a/65012723
vals = [2,3,5]
sb.relplot(mtsf_long.loc[mtsf_long.value_index.isin(vals)],
           x = "culminative_time", 
           y = "timbre",
           kind = "line",
           col = "value_index",
           hue = "value_index", ) 
#%%
sb.lineplot(mtsf_long.loc[mtsf_long.value_index.isin(vals)],
           x = "culminative_time", 
           y = "timbre", "loudness_max",
           hue = "value_index",)
### ---

#%%    
###############################################################################
####                            Graphs                                     ####
###############################################################################

#%%    create our ax
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

#%%
# RATHER LEARN MATPLOTLIB  AND fig,ax things before "seaborn" 

# double plotting in matplotlib: https://matplotlib.org/stable/gallery/lines_bars_and_markers/cohere.html#sphx-glr-gallery-lines-bars-and-markers-cohere-py

"""
# https://stackoverflow.com/a/8228808
 - plt.cla() clears an axis, i.e. the currently active axis in the current figure. It leaves the other axes untouched.
 - plt.clf() clears the entire current figure with all its axes, but leaves the window opened, such that it may be reused for other plots.
 - plt.close() closes a window, which will be the current window, if not specified otherwise.

# Thus we can make ONE FIGURE, ADD TO IT (ax) and clear it! 
"""
# add loudness - do something fancy here
ax.plot(mtsf["culminative_time"], mtsf["loudness_max"])

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


#%%<<<<<<zzzz
f2, ax1 = sb

test = sb.relplot(my_top_song_features, x = "culminative_time", y = "timbre-1", kind = "line")

test.set_titles("test")



test.axes_dict.items()

ax = sb.relplot(my_top_song_features, x = "culminative_time", y = "pitch-7", kind = "line")

sb.relplot(my_top_song_features, x = "culminative_time", y = "timbre-2", kind="line")

sb.relplot(my_top_song_features, x = "culminative_time", y = "timbre-3", kind="line")




#%%
fig.tight_layout()
plt.show()
fig














