# Spotify Project

Repository for exam in course "PSY-3035 - Programming and Data Visualization for Researchers" at UiT - The Arctic University of Norway (https://uit.no/utdanning/emner/emne/785298/psy-3035).

# Spotify Visualizing
A simple script to visualize my top Spotify songs from 2022 against the top tracks of the world in 2022. 

## Data
The script checks if the data is saved in the local "data" folder and retreives the data - if not retreives the data from the Spotify API. 

The data consists of both the my and the worlds top songs (100 and 50 respectively) and data regarding the features of each playlist. 


Running the main script "Spotify_Visualizing.py" under the "src" folder should do all the work: It will (1) get set the working directory relative to the position of the script, (2) read all the data necessary to create the plots and then (3) create three different plots. 

## Visualizing
For the visualizing part below, only the data "my_top_tracks_2022.csv", "my_top_tracks_2022_features.csv", "top_tracks_world_2022.csv" and "top_tracks_world_features_2022.csv" are used. Although some additional data can be fond there

For the visualizing part, we plot the track feautres of each playlist against each other.

### First plot
For the first plot, we check the top 20 songs of each playlist and map the "danceability" per track on a dotplot.

Given that the plot is not that informative regarding the differences, we proceed to look at the general differences.

### Second plot
For the second plot we look at the general differences across the playlist features of the top 50 tracks (max tracks for the World playlist).

Relevant transformations of the data take place before visualizing. Such as removing uninformative columns and combining the two dataframes. 

### Third plot


## Extra Functions:
In the "lib" folder there is a script containing some extra functions to get out data to a dataframe 
- last_played_df
	- Input: sp
	- Get the last (50) played songs and add them to a dataframe (pandas).
	- Require spotify user authentication call (typically "sp")
- playlist_to_df
	- Input: playlist(id, uri or url) 
	- Get a specific playlist and put it in a dataframe.
	- Require base spotify authentication for public playlists or user authentication for private playlists (typically "sp").
- top_artists_df
	- Input: sp
	- Get the top artists of the current authenticated user and put it in a dataframe.
	- Require user authentication call (typically "sp").
- top_tracks_df
	- Input: sp (OPTIONAL: limit, time_range) 
		- time_range can be either "long_term", "middle_term" or "short_term".
	- Get the top tracks of the current authenticated user and put it in a dataframe.
	- Require user authentication call (typically "sp").
- track_analysis_to_df
	- Input: sp, list(id, uri or url)
	- Get raw audio analysis and put it in a dataframe.
	- Require either base 