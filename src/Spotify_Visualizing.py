# -*- coding: utf-8 -*-
"""
### To-do ###
- [x] make culminative time ! so we can see whe nin the song we are lookin at 

"""
# %% Quick run
#### Set environment
import os
if os.path.exists("D:/coding/GitHub/a-asen/spotify_project"):  # School
    path = "D:/coding/GitHub/a-asen/spotify_project"
if os.path.exists("D:/_coding/GitHub/a-asen/Spotify_Visualizing"):  # Home
    path = "D:/_coding/GitHub/a-asen/Spotify_Visualizing"

os.chdir(path)  # change directory
print(os.getcwd())  # get change

#### Packages
import json
import pandas as pd
import spotipy
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import lib.spotify_to_df as lib #local library
    # lib.top_tracks_df(sp) 
    # https://codeigo.com/python/import-function-from-file # better & more
    # https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file

#### Read Keys & accessories
with open("access/access_token.json", "r") as f: # Get client ID and secret
    access_token = json.load(f)

# Redirect link:
sp_redirect = "http://localhost:8888/callback"
# Scopes (things we want to access - the "scope of our acccess")
sp_scopes = "user-read-playback-state,user-read-currently-playing,user-read-playback-position,user-top-read,user-read-recently-played,playlist-read-private,playlist-read-collaborative"

# https://developer.spotify.com/documentation/general/guides/authorization/scopes/
# https://spotipy.readthedocs.io/en/2.22.1/#spotipy.oauth2.SpotifyOAuth.__init__

#### User Authentication
# https://spotipy.readthedocs.io/en/2.22.1/#spotipy.oauth2.SpotifyOAuth.__init__
sp_user_auth = spotipy.SpotifyOAuth(
    client_id       =  access_token["Client_ID"],     # client ID
    client_secret   =  access_token["Client_Secret"], # Secret
    redirect_uri    =  sp_redirect,                   # redirect to....
    scope           =  sp_scopes)                     # access scope

#sp_user_auth.get_auth_response()

#### Authentication Call
# Set the "auth_manager" to our credentials according to the given "auth" access
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
# We set our access point to "sp" by authorizing with "sp_user_auth"

sp = spotipy.Spotify(auth_manager = sp_user_auth)

#sp_user_auth.get_auth_response() # these should authorize if it doesnt happen automatically
#sp_user_auth.get_authorization_code()

####  Read  //  Get data

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


########################
#### ||||   Graph   ||||
########################
# %% Lineplot 
fig1, ax1 = plt.subplots()

#### Data shorthand 
lineplot_my = mtt22f.iloc[0:20,]
lineplot_world = wtt22f.iloc[0:20,]

plt.figure(1)
# DATA PLOTTING
#  https://www.color-hex.com/color/00a170
ax1.plot(lineplot_my.index, lineplot_my["danceability"], c ="#32b38c", linewidth = 3)
ax1.plot(lineplot_world.index, lineplot_world["danceability"], c ="red", linewidth = 2, linestyle = "dotted")

####   ax1 CHANGES
ax1.set_facecolor("lightgrey")
ax1.grid()
ax1.set_yticks(np.arange(0.4,1,0.05))
ax1.set_xticks(np.arange(1,21,1))
plt.ylim(0.4,0.95) # https://www.geeksforgeeks.org/matplotlib-pyplot-ylim-in-python/
plt.xlim(1,20)  # but why plt and not ax1/fig?

# INFO
fig1.legend(loc = "right", labels = ["My Top 20","World Top 20"])
ax1.set_title("Danceability", size = 16)

ax1.set_xlabel("Song rank", size = 12)
ax1.set_ylabel("Danceability score", size = 12)

# %%  BOXPLOT
#### Data
# My data
boxplot_my = mtt22f.iloc[0:50]
boxplot_my = boxplot_my.reset_index() # index column
boxplot_my = boxplot_my.drop(columns = ["mode", "key", "uri", "tempo", "duration_ms", "time_signature", "instrumentalness", "loudness"])
boxplot_my = pd.melt(frame = boxplot_my,
             id_vars = "index", value_vars = boxplot_my.columns[0:14], 
             var_name = "variable", value_name = "value")

means = boxplot_my.groupby("variable")["value"].mean().reset_index()
means = means.sort_values("value")
boxplot_my["variable"] = boxplot_my["variable"].astype(pd.CategoricalDtype(categories = means["variable"], ordered = True))
boxplot_my = boxplot_my.sort_values("variable")
boxplot_my["from"] = "My top"

# World data
boxplot_world = wtt22f.iloc[0:50]
boxplot_world = boxplot_world.reset_index() # index column
boxplot_world = boxplot_world.drop(columns = ["mode", "key", "uri", "tempo", "duration_ms", "time_signature", "instrumentalness", "loudness"])
#boxplot_world["loudness"] = np.log10(np.sqrt(boxplot_world["loudness"]**2))
boxplot_world = pd.melt(frame = boxplot_world,
             id_vars = "index", value_vars = boxplot_world.columns[0:14], 
             var_name = "variable", value_name = "value")

means = boxplot_world.groupby("variable")["value"].mean().reset_index()
means = means.sort_values("value")
boxplot_world["variable"] = boxplot_world["variable"].astype(pd.CategoricalDtype(categories = means["variable"], ordered = True))
boxplot_world = boxplot_world.sort_values("variable")
boxplot_world["from"] = "World top"

dp3 = pd.concat([boxplot_my, boxplot_world], axis = 0)


###  VIOLIN PLOT -- 
# plt.cla()
# sb.violinplot(dp3, y = "variable", x = "value", hue = "from", width = 1)

#### BOXPLOT -- Figure information
fig2, ax2 = plt.subplots()
plt.figure(2)
ax2 = sb.boxplot(dp3, y = "variable", x = "value", hue = "from", dodge = True, ax=ax2)
sb.despine(trim = True, ax=ax2)
ax2.grid(axis = "x", alpha = .7, linestyle = "solid") 
ax2.set_axisbelow(True) # draw lines behind
ax2.set_xticks(np.arange(0.0,1.1,0.1))

ax2.set_xlabel("Percent confidence", size = 16, labelpad = 16)
#fig2.suptitle("Music features over 'My top' and 'World top' tracks", size = 22)
ax2.set_title("Music features over 'My top' and 'World top' tracks", size = 22, pad = 18) # 

ax2.legend(title = "", fontsize = 12) 
ax2.set_yticklabels(["Instrumentalness", "Speechiness", "Acousticness", "Liveness", "Valence", "Danceability", "Energy"])
ax2.set_xticklabels(np.arange(0,101,10))

#ax2.tick_params(labelsize = 12) 

#%%  CORRELATION
import scipy.stats as s
fig3, ax3 = plt.subplots()

dp = mtt22f[0:50]
dp2 = wtt22f
dp["loudness"] = np.log10(np.sqrt(dp["loudness"]**2))
dp2["loudness"] = np.log10(np.sqrt(dp2["loudness"]**2))
dp = dp.drop(columns = ["key", "mode", "uri","tempo","duration_ms","time_signature"])

df = dp.corr() # create a correlation matrix

mask = np.triu(np.ones_like(df, dtype=bool))         # mask (only half of all corrs)
cmap = sb.diverging_palette(230, 20, as_cmap=True)   # colour map

plt.clf()
ax3 = sb.heatmap(df, mask = mask, cmap = cmap, linewidths=.5, annot = True,)
ax3.xaxis.tick_top() # Flip to top
plt.xticks(rotation=25) # rotate
ax3.grid(which="minor")


#%%
#####
plt.plot(dp.index[0:21], dp["loudness"][0:21],) # plot loudness on a graph? 
dp.columns
dp.corr() # LUL that was easy 
dp.columns
s.pearsonr(dp["loudness"], dp["energy"])
s.pearsonr(dp["loudness"], dp["danceability"])
s.pearsonr(dp["loudness"], dp["speechiness"])
s.pearsonr(dp["loudness"], dp["valence"])
s.pearsonr(dp["loudness"], dp["instrumentalness"])
s.pearsonr(dp["loudness"], dp["liveness"])
s.pearsonr(dp["loudness"], dp["tempo"])


plt.scatter(dp["energy"], dp["loudness"])
plt.scatter(dp["energy"], dp["danceability"])

plt.plot(dp["energy"], )
#######









