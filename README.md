# Spotify Project

Repository for exam in course "PSY-3035 - Programming and Data Visualization for Researchers" at UiT - The Arctic University of Norway (https://uit.no/utdanning/emner/emne/785298/psy-3035).

# Spotify Visualizing
A simple script to visualize my top Spotify songs from 2022 against the top tracks of the world in 2022. 

## Data
The script checks if the data is saved in the local "data" folder and retreives the data - if not retreives the data from the Spotify API. 

The data consists of both the my and the worlds top songs (100 and 50 respectively) and data regarding the features of each playlist. 

## Visualizing
For the visualizing part, we plot the track feautres of each playlist against each other.

### First plot
For the first plot, we check the top 20 songs of each playlist and map the "danceability" per track on a dotplot.

Given that the plot is not that informative regarding the differences, we proceed to look at the general differences.

### Second plot
For the second plot we look at the general differences across the playlist features of the top 50 tracks (max tracks for the World playlist).

Relevant transformations of the data take place before visualizing. Such as removing uninformative columns and combining the two dataframes. 

### Third plot


