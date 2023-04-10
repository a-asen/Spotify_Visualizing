# -*- coding: utf-8 -*-
"""
"""
####                            Packages                                   ####
import os
# This should enable us to run this script form anywhere and it should automatically set 
# the working directory to the correct path. 
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
# stricly speaking, running the file from anywhere should set the working directory to the files path, 
# and thus only one "path.dirname" is required over the "__file__" 

import json
import pandas as pd
import spotipy
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import lib.function_package as lib #local library
    # lib.top_tracks_df(sp) 
    # https://codeigo.com/python/import-function-from-file # better & more
    # https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file

#######################         TOGGLES            ############################
skip_authorization = True
    # We do not need to setup any authentication given that the data is available. 
    # For this reason "skip_authorization" is set to true. 

spotify_basic_authorization = True  # only relevant if "skip_authentication is False"
# False to get "private", or personalized data (e.g., top artists/tracks)   
    # I needed "user authentication" in order to get my "top 2022" playlist. 
    # It is not possible for others "user authentication" to get my private playlists
    # and so basic authorisation is enough because the data is saved under the "data" folder

include_all = False  # If True you get two more plotted values 

# Not implemented
#override_figure = False  # Default is "False"
#   # I do not want to override my own, already exisiting figure


if include_all == True: # columns to be dropped for later plotting
    drop = ["mode", "key", "uri", "duration_ms", "time_signature", "tempo"]
else:
    drop = ["mode", "key", "uri", "duration_ms", "time_signature", "tempo", "instrumentalness", "loudness"]

###############################################################################
####                       Setup Spotify API calls                         ####
if skip_authorization == False: 
    # Read keys
    with open("access/access_token.json", "r") as f:
        access_token = json.load(f)

    if spotify_basic_authorization == True: 
        sp = spotipy.Spotify(auth_manager = spotipy.oauth2.SpotifyClientCredentials(
            client_id = access_token["Client_ID"],
            client_secret = access_token["Client_Secret"]))
    else:
    # If we do NOT use basic authentication, we set up the authorization calls according to this:
        sp_redirect = "http://localhost:8888/callback"  # Set redirect link
        # Scopes (things we want to access - the "scope of our acccess")
        # backslash (\) breaks the line, making it easier to read.
        sp_scopes = "user-read-playback-state,user-read-currently-playing,\
        user-read-playback-position,user-top-read,user-read-recently-played,\
        playlist-read-private,playlist-read-collaborative"
        
        # https://developer.spotify.com/documentation/general/guides/authorization/scopes/
        # https://spotipy.readthedocs.io/en/2.22.1/#spotipy.oauth2.SpotifyOAuth.__init__
        
        #### User Authentication
        # https://spotipy.readthedocs.io/en/2.22.1/#spotipy.oauth2.SpotifyOAuth.__init__
        sp_user_auth = spotipy.SpotifyOAuth(
            client_id       =  access_token["Client_ID"],     # client ID
            client_secret   =  access_token["Client_Secret"], # Secret
            redirect_uri    =  sp_redirect,                   # redirect to....
            scope           =  sp_scopes)                     # access scope
    
        #sp_user_auth.get_auth_response() # these should authorize if it doesnt happen automatically
        #sp_user_auth.get_authorization_code()
        
        #### Authentication Call
        # Set the "auth_manager" to our credentials according to the given "auth" access
        # https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
        # We set our access point to "sp" by authorizing with "sp_user_auth"
        
        sp = spotipy.Spotify(auth_manager = sp_user_auth) # set our authorization calls
        

###############################################################################
####                        Read  //  Get data                            #####
    
#           NO NEED TO LOAD THE API UNNECESSARIY
# We check if we have the data stored in a .csv file and read it.
# IF NOT, we do API calls to get the data and store it in the "data" folder 

#########             WORLD TOP TRACKS 2022!             ##############
### world top tracks 2022 (wtt22)
# only come with top 50 tracks
if os.path.exists("data/top_tracks_world_2022.csv"):
    wtt22 = pd.read_csv("data/top_tracks_world_2022.csv", index_col = 0) # Get col index. More pleasing to work with 
    wtt22.name = "wtt22"
else:
    wtt22 = lib.playlist_to_df(sp, "37i9dQZF1DX18jTM2l2fJY")
    wtt22 = wtt22.set_index(wtt22.index + 1)      # set new index
    wtt22.name = "wtt22"
    wtt22.to_csv("data/top_tracks_world_2022.csv")

##########          World top tracks 2022 FEATURES       ##############
if os.path.exists("data/top_tracks_world_2022_features.csv"):
    wtt22f = pd.read_csv("data/top_tracks_world_2022_features.csv", index_col = 0)
    wtt22f.name = "wtt22f"
else:
    wtt22f = sp.audio_features(wtt22["uri"])
    wtt22f = pd.DataFrame(wtt22f)
    wtt22f = wtt22f.drop(["id","track_href", "analysis_url","type"], axis = 1) # drop useless columns
    wtt22f = wtt22f.set_index(wtt22f.index + 1)
    wtt22f.name = "wtt22f"
    wtt22f.to_csv("data/top_tracks_world_2022_features.csv")


########            My Top Tracks 2022 (mtt22)           ############# 
if os.path.exists("data/my_top_tracks_2022.csv"):
    mtt22 = pd.read_csv("data/my_top_tracks_2022.csv", index_col = 0)
    mtt22.name = "mtt22"
else:
    mtt22 = lib.playlist_to_df(sp, "37i9dQZF1F0sijgNaJdgit")
    mtt22 = mtt22.set_index(mtt22.index + 1)      # set new index
    mtt22.name = "mtt22"
    mtt22.to_csv("data/my_top_tracks_2022.csv")

########       My Top Tracks 2022 Features (mtt22f)       #############
if os.path.exists("data/my_top_tracks_2022_features.csv"):
    mtt22f = pd.read_csv("data/my_top_tracks_2022_features.csv", index_col = 0)
    mtt22f.name = "mtt22f"
else:
    mtt22f = sp.audio_features(mtt22["uri"])
    mtt22f = pd.DataFrame(mtt22f)
    mtt22f = mtt22f.drop(["id","track_href", "analysis_url","type"], axis = 1) # drop useless columns
    mtt22f = mtt22f.set_index(mtt22f.index + 1)
    mtt22f.name = "mtt22f"
    mtt22f.to_csv("data/my_top_tracks_2022_features.csv")

# %% Line plot run cell
###############################################################################
####                            Line plot                                  ####       
fig1, ax1 = plt.subplots() # Create a plot

# Subsetting data: 
    # We use only top 20 of world and my songs from 2022
lineplot_my = mtt22f.iloc[0:20,]        
lineplot_world = wtt22f.iloc[0:20,]

# Plotting the data
#  https://www.color-hex.com/color/00a170
ax1.plot(lineplot_world.index, lineplot_world["danceability"], c ="#FF0000", linewidth = 3, linestyle = "dotted")
ax1.plot(lineplot_my.index, lineplot_my["danceability"], c ="#228B22", linewidth = 4)

# Axis changes
ax1.set_facecolor("lightgrey")      # gray background
ax1.grid()                              # add a grid
ax1.set_yticks(np.arange(0.4,1,0.05))   # new ticks for the y axis
ax1.set_xticks(np.arange(1,21,1))       # new ticks for the x axis
plt.ylim(0.4,0.95)                      # limit the y axis 
# https://www.geeksforgeeks.org/matplotlib-pyplot-ylim-in-python/
plt.xlim(1,20)                          # Limit the x axis

# Axis info
fig1.legend(labels = ["World Top 20","My Top 20"], fontsize = 14,  # Legend name/size
            loc = "center",  # general position 
            bbox_to_anchor = (0.62,0.625,0.5,0.5))  # relative position to the general position
ax1.set_title("Danceability of the top 20 tracks for each playlist", size = 22)  # axis title

ax1.set_xlabel("Song rank", size = 16)      # X title
ax1.set_ylabel("Danceability score", size = 16)   # Y title
ax1.tick_params(labelsize = 14)   # increase x/y tick labels

fig1.set_size_inches(14,8)  # Set a bigger figure size
fig1.subplots_adjust(left = .075,  right  = .95, top  = .94,  bottom = .08)  # Fit the axis to the figure.

# Save figure if it does not exist
if os.path.exists("fig/figure-1_lineplot.png"):
    pass
else:
    fig1.savefig("fig/figure-1_lineplot.png")

# %%  Box plot run cell 
###############################################################################
####                         Box plotting                                  ####
# My data
sub_my = mtt22f.iloc[0:50]  # subset songs
boxplot_my = sub_my.reset_index() # create an index column

boxplot_my = boxplot_my.drop(columns = drop)  # remove useless columns 
stats_tests = boxplot_my.columns[1:len(boxplot_my)] # used for later tests
if "loudness" in boxplot_my.columns: # if loudness is in the columns, transform it
    # First we transform the negative "loudness" values to positive by taking the absolute power
    # Then we take the logarithmic value of it to fit it neatly into our boxplot. 
    # This should preserve the actual value but still make it plottable for our case. 
    boxplot_my["loudness"] = np.log(np.log(abs(boxplot_my["loudness"]))) # for plotting
    sub_my["loudness"] = np.log(np.log(abs(sub_my["loudness"]))) # for stats

# Collapse the wide dataframe to a long dataframe (for plotting the data) 
boxplot_my = pd.melt(frame = boxplot_my,
             id_vars = "index",  # Each values is indexed by "index"
             value_vars = boxplot_my.columns[0:14],  # all the values we are collapsing by
             var_name = "variable",     # The names of each variable is stored under "variable"
             value_name = "value")      # The values of each datapoint is stored under "value"
boxplot_my["from"] = "My top" # creating a new row, used to distinguish my and world data 

# World data
# same procedure as above, for the world data
sub_world = wtt22f
boxplot_world = sub_world.reset_index() 
boxplot_world = boxplot_world.drop(columns = drop)
if "loudness" in boxplot_world.columns: 
    boxplot_world["loudness"] = np.log(np.log(abs(boxplot_world["loudness"])))
    sub_world["loudness"] = np.log(np.log(abs(sub_world["loudness"])))
boxplot_world = pd.melt(frame = boxplot_world,
             id_vars = "index", value_vars = boxplot_world.columns[0:14], 
             var_name = "variable", value_name = "value")
boxplot_world["from"] = "World top"

# We then combine these two dataframes in one long dataframe
dp3 = pd.concat([boxplot_my, boxplot_world], axis = 0) 

# We want to order the layout of each category (e.g., danceability) according to some order (acending/descending)
# for this we need to know their average values
means = dp3.groupby("variable")["value"].mean().reset_index() #
names = means = means.sort_values("value")
# Then we take these values and order the "variable" according to this by 
# creating an ordered categorical variable (that is the "variable")
dp3["variable"] = dp3["variable"].astype(pd.CategoricalDtype(categories = means["variable"], ordered = True))
# From that we can then sort the variable. 
dp3 = dp3.sort_values("variable")

# visualizing
fig2, ax2 = plt.subplots()  # new plot
fig2.set_size_inches(14,8)  # Set a bigger figure size

# plotting the data:
    # We want to plot each "variable" according to the "value" they correspond to
    # split by where they are "from" (i.e., my playlist or the world playlist)
ax2 = sb.boxplot(dp3, y = "variable", x = "value", hue = "from", dodge = True, ax = ax2)
sb.despine(trim = True, ax = ax2)  # simplify the graph, removes a couple of lines
ax2.grid(axis = "x", alpha = .7, linestyle = "solid")  # lines from the x axis
ax2.set_axisbelow(True) # draw lines behind
ax2.set_xticks(np.arange(0.0,1.1,0.1))  # new ticks for the x axis

# Graph information:
# title
ax2.set_title("Music features over 'My top' and 'World top' tracks", size = 26, pad = 18)
# x/y labels
ax2.set_xlabel("Percent confidence", size = 20, labelpad = 16) 
ax2.set_ylabel("")  # remove useless label

ax2.legend(title = "", fontsize = 12)  # remove legend title & increase size

# fixup ytick labels
ax2.set_yticklabels(names["variable"].str.capitalize()) 
ax2.set_xticklabels(np.arange(0,101,10)) # new x ticks labels in percent form 

ax2.tick_params(labelsize = 14)  # increase x/y tick size
fig2.subplots_adjust(left = .1,  right  = .95, top  = .91,  bottom = .1)  # Fit the axis to the figure.

# Save figure if it do not exists
if os.path.exists("fig/figure-2_boxplot.png"):
    pass
else:
    fig2.savefig("fig/figure-2_boxplot.png")

####  Table statistic 
table = lib.ttest_to_table(mtt22f.iloc[0:50], wtt22f, drop)
if os.path.exists("data/t-test_table.xlsx"):
    pass
else:
    table.to_excel("data/t-test_table.xlsx")

#%%   Correlation matrix run cell
###############################################################################
####                    Correlation Matrix                                 ####
####  Figure 3 - My data
cmap = sb.diverging_palette(220, 10, as_cmap = True)   # common colorbar palette
fig3, ax3 = plt.subplots(figsize = (10,8))  # 

dp = mtt22f[0:50]
dp = dp.drop(columns = drop)
df = dp.corr()                                      # create a correlation matrix
df.columns = dp.columns.str.capitalize().to_list()  # change x names
df.index = dp.columns.str.capitalize().to_list()    # change y namse

mask1 = np.triu(np.ones_like(df, dtype = bool))         # mask (only half of all corrs)

ax3 = sb.heatmap(df, mask = mask1, cmap = cmap, linewidths = 1, annot = True,
                 square = True,  # Force squared distances
                 annot_kws = {"fontsize":16}, ) # size of correlation values
                 #cbar_kws = {"location": "top", "aspect": 20, "labelsize": 14})
                 
ax3.xaxis.tick_top()         # Flip x ticks to the top
plt.xticks(rotation = 25)    # rotate x axis slightly 
plt.yticks(rotation = 0)     # rotate y axis horizontal
ax3.tick_params(labelsize = 16) # tick label size increase 

ax3.set_title("My features correlation matrix", size = 26, pad = 20) # set title of the figure
fig3.subplots_adjust(left = .17,  right  = .97, top  = .80,  bottom = .02)  # Fit the axis to the figure.

# Save figure if it does not exist
if os.path.exists("fig/figure-3_my_corr_matrix.png"):
    pass
else: 
    fig3.savefig("fig/figure-3_my_corr_matrix.png")
    
#### Figure 4 - World data
fig4, ax4 = plt.subplots(figsize = (10,8))

dp2 = wtt22f
dp2 = dp2.drop(columns = drop)
df2 = dp2.corr()
df2.columns = dp2.columns.str.capitalize().to_list()
df2.index = dp2.columns.str.capitalize().to_list()

# Mask & plot
mask2 = np.triu(np.ones_like(df2, dtype = bool))
ax4 = sb.heatmap(df2, mask = mask2, cmap = cmap, linewidths = 1, annot = True,
                 square = True,
                 annot_kws = {"fontsize":16}, )
                 #cbar_kws = {"location": "top", "aspect": 20, "labelsize": 14})

ax4.xaxis.tick_top()        # Flip to top
plt.xticks(rotation = 25)   # rotate
plt.yticks(rotation = 0)    # rotate
ax4.tick_params(labelsize = 16)

ax4.set_title("World features correlation matrix", size = 26, pad = 20)
fig4.subplots_adjust(left = .17,  right  = .97, top  = .80,  bottom = .02)  # Fit the axis to the figure.

# Save figure if it does not exist
if os.path.exists("fig/figure-4_world_corr_matrix.png"):
    pass
else: 
    fig4.savefig("fig/figure-4_world_corr_matrix.png")

