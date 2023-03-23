# -*- coding: utf-8 -*-
import pandas as pd


# %%  Get Recently Played
# https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recently-played
def last_played_df(sp, limit: int = 50): # https://stackoverflow.com/questions/61893276/can-i-define-both-functions-arguments-default-value-and-data-type-in-python
    """
    Get users recently played songs.
    - Input: 
        - sp: Spotify authorization object (user)
        - limit: Amount of tracks to retrieve (max 50)
     - Output: Pandas Dataframe 
    
    NOTE:
    This function require user authentication object ( see: https://spotipy.readthedocs.io/en/2.22.1/#module-spotipy.oauth2 ) 
    
    # Example: 
    my_recently_played = last_played_df(sp)
    """
       
    user_recently_played = sp.current_user_recently_played(limit=limit)  # get users last played (limit = 50)
    
    dl_recently = []                            # Empty list
    for item in user_recently_played["items"]:  # Parse dictionary
        d = {}                                      # New dict
        d["played_time"] = item["played_at"]        # Get play time
        d["track_title"] = item["track"]["name"]    # Get track title
        d["artists"] = []
        for artist in item["track"]["artists"]:     # Get each artist to a list in a dict
            d["artists"].append(artist["name"])
        d["popularity"] = item["track"]["popularity"]   # Get the popularity
        d["uri"] = item["track"]["uri"]             # Get the track URI
        d["duration"] = item["track"]["duration_ms"]    # Get duration of the track
        dl_recently.append(d)                           # Append to the list
    return(pd.DataFrame(dl_recently))               # Return the dataframed list


# %%  Get "a" playlist tracks
def playlist_to_df(sp, playlist_id: str):
    """
    Get a songs in a specific playlist.
     - Input:  
        - sp: Spotify authorization object (base/user)
        - playlist_id: Playlist string either **ID**, **URI** or **URL** 
     - Output: Pandas dataframe
     
    NOTE: 
    Public playlists only require basic authentication ( see: https://spotipy.readthedocs.io/en/2.22.1/#client-credentials-flow ).
    Private playlists require user authentication ( see: https://spotipy.readthedocs.io/en/2.22.1/#module-spotipy.oauth2 ).
    
    # Example:
    playlist = user_playlist_to_df(sp, "37i9dQZF1DXaWf8ZIHreXF") # Spotify "Dance Hits 2010s"
    """
    
    playlist_tracks = sp.playlist_tracks(playlist_id)  # 2022 playlist

    dl_playlist = []
    for item in playlist_tracks["items"]:
        d = {}
        d["track_title"] = item["track"]["name"]
        d["artists"] = []
        for artist in item["track"]["artists"]:
            d["artists"].append(artist["name"])
        d["popularity"] = item["track"]["popularity"]
        d["uri"] = item["track"]["uri"]
        d["duration"] = item["track"]["duration_ms"]
        d["added_by"] = item["added_by"]["id"]
        d["added_at"] = item["added_at"]
        dl_playlist.append(d)
    return(pd.DataFrame(dl_playlist))


# %%  Top artists
def top_artists_df(sp):
    """
    Get users top artists.
    - Input:  
        - sp: Spotify authorization object (user)
     - Output: Pandas dataframe
    
    NOTE:
    This function requires user authentication object (see: https://spotipy.readthedocs.io/en/2.22.1/#module-spotipy.oauth2 ) 
        
    # Example:
    top_artists = user_top_artists_df(sp)
    """
    
    top_artists = sp.current_user_top_artists()

    dl_artists = []
    for item in top_artists["items"]:
        d = {}
        d["name"] = item["name"]
        d["popularity"] = item["popularity"]
        d["genres"] = item["genres"]
        dl_artists.append(d)
    return(pd.DataFrame(dl_artists))


# %%   Top tracks
def top_tracks_df(sp, limit: int = 50, time_range: str = "medium_term"):
    """
    Get users top tracks.
    - Input:  
        - sp: Spotify authorization object (user)
        - limit: Amount of top tracks (max 50)
        - time_range: Period of time (short_term = 4 weeks; medium_term = 6 months; long_term = several years)
     - Output: Pandas dataframe
    
    NOTE:
    This function requires user authentication object ( see: https://spotipy.readthedocs.io/en/2.22.1/#module-spotipy.oauth2 )
    
    # Example:
    top_tracks = user_top_tracks_df(sp)
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


# %%  Get song analysis
def track_analysis_to_df(sp, audio_list: list, str):
    """
    Get raw audio analysis of a list of songs (ID, URI, URL)
    (Can be of a single song, but needs to be given in a list)
     - Input:  
        - sp: Spotify authorization object (base/user)
        - audio_list: List or string of **ID**, **URI** or **URL** 
     - Output: Pandas dataframe
    
    NOTE:
    Either authentication object work.
        (base: https://spotipy.readthedocs.io/en/2.22.1/#client-credentials-flow ; 
         user: https://spotipy.readthedocs.io/en/2.22.1/#module-spotipy.oauth2 )
    
    # Example:
    track_analysis = track_analysis_to_df(sp, <my_top_tracks["uri"]>)
    """
    
    data_list = []  # where we put our informatio
    for enu, song in enumerate(audio_list):  # For each
        analysis = sp.audio_analysis(song)
        for enu2, item in enumerate(analysis["segments"]):
            d = {}
            d["song index"]     = enu
            d["track index"]    = enu2
            d["time"]           = item["duration"]
            d["loudness_time"]  = item["loudness_max_time"]
            d["loudness_max"]   = item["loudness_max"]
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



