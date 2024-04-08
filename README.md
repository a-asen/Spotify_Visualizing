# Spotify Visualizing

Repository for exam in course "PSY-3035 - Programming and Data Visualization for Researchers" at UiT - The Arctic University of Norway (https://uit.no/utdanning/emner/emne/785298/psy-3035).

A repository with simple scripts to visualize Spotify data. 

The script "Spotify_Visualizing" under "src" named can immediately be run to produce the figures under "fig". 

## Citing:
Aasen, S., R. (2023). Python Data Visualization, https://github.com/a-asen/Spotify_Visualizing


## Toggles
The script is currently set up to run immediately and reproduce the figure under "fig". The script has 3 toggles: 
1. "skip_authorization" will skip the Spotify authorization process (True) or not (False).
2. "spotify_basic_authorization" which is used to authorize either basic access (True) or user access (False).
3. "boxplot_include_all" will add two extra features to the box plot (True) which has otherwise been left out (False).

## Data
The script will checks if there is existing data in the "data" folder. This is to be able to use the same data that I use to visualize. 
If you want your own data you can delete/rename "my_top_tracks_2022.csv" and "my_top_tracks_2022_features.csv". Alternatively you can change the saving/checking names in the script to get your own data. 
	_* Note: Only "my" data has to be deleted/renamed/moved if you compare your own data against the world 2022._

The data stored under "data":
- My top songs (100 tracks) 
    - "my_top_tracks_2022.csv" 
    - "my_top_tracks_2022_features.csv", 
- World top songs (50 tracks)
    - "top_tracks_world_2022.csv" 
    - "top_tracks_world_features_2022.csv"
- "t-test_table.xlsx" is a saved table

## Script
Running the main script "Spotify_Visualizing.py" under the "src" folder should recreate all figures under "fig". 
It will:
1. Read all the data necessary to create the plots 
2. Create four plots
    - These plots are available under the "fig" folder.

## Visualizing
We plot the track features of each playlist against each other.

### First plot
For the first plot, we check the top 20 songs of each playlist and map the "danceability" per track on a line plot. The two datasets were split by colour and line type: green & whole (my data) and orange and dotted (world data)
![Lineplot](/fig/figure-1_lineplot.png)

### Second plot
For the second plot, we look at the general differences across the playlist features of the top 50 tracks (max tracks for the World playlist).

Relevant transformations of the data are done before the visualizing part. Such as removing uninformative columns and combining the two data frames. 
![Boxplot](/fig/figure-2_boxplot.png)

### Third & fourth plot
For the third and fourth plot, we create a correlation matrix for each dataset. Each plot looks at the correlations between song features within each playlist.

| My Playlist | World Playlist |
|---|---|
|![My Correlation Matrix](/fig/figure-3_my_corr_matrix.png) | ![World Correlation Matrix](/fig/figure-4_world_corr_matrix.png) |


## Extra Functions:
A function script is found under "lib" and can be accessed with the "lib" shorthand. It contains both functions to get data to a data frame, and some extra functions if you want to further explore your own data/other data. 
- last_played_df
	- Input: sp
	- Get the last (50) played songs and add them to a data frame (pandas).
	- Require Spotify user authentication call (typically "sp")
	- Output: Pandas data frame
- playlist_to_df
	- Input: sp; playlist(ID, URI or URL) 
	- Get a specific playlist and put it in a data frame.
	- Require base Spotify authentication for public playlists or user authentication for private playlists (typically "sp").
	- Output: Pandas data frame
- top_artists_df
	- Input: sp
	- Get the top artists of the current authenticated user and put it in a data frame.
	- Require user authentication call (typically "sp").
	- Output: Pandas data frame
- top_tracks_df
	- Input: sp; (OPTIONAL: limit; time_range)
		- time_range can be either "long_term", "middle_term" or "short_term".
	- Get the top tracks of the current authenticated user and put it in a data frame.
	- Require user authentication call (typically "sp").
	- Output: Pandas data frame
- track_analysis_to_df
	- Input: sp, list(ID, URI or URL)
	- Get raw audio analysis and put it in a data frame.
	- Require either base 
	- Output: Pandas data frame
- ttest_to_table
	- Input: data frame 1, data frame 2, drop list
	- Test the difference between each data frame of similar column names
	- Output: Pandas data frame
