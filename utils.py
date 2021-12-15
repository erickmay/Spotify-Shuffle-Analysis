import pandas as pd

def clean_data(songs_df):
    songs_df = songs_df[songs_df["shuffle"] != False]

    songs_df["ts"] = songs_df["ts"].astype(str)
    songs_df = songs_df[~(songs_df["ts"].str.contains("2014"))]
    songs_df = songs_df[~(songs_df["ts"].str.contains("2015"))]
    songs_df = songs_df[~(songs_df["ts"].str.contains("2016"))]
    songs_df = songs_df[~(songs_df["ts"].str.contains("2017"))]
    songs_df = songs_df[~(songs_df["ts"].str.contains("2018"))]
    songs_df = songs_df[~(songs_df["ts"].str.contains("2019"))]
    songs_df = songs_df[~(songs_df["ts"].str.contains("2020-01"))]
    songs_df = songs_df[~(songs_df["ts"].str.contains("2020-02"))]
    songs_df = songs_df[~(songs_df["ts"].str.contains("2020-03"))]

    return songs_df

def create_value_counts_table(songs_df):
    unique_songs_df = songs_df["master_metadata_track_name"].value_counts()
    unique_songs_df = unique_songs_df.rename_axis("master_metadata_track_name").reset_index(name="counts")

    return unique_songs_df

def outer_join(unique_songs_df, playlist_df):
    tracks_df = unique_songs_df.merge(playlist_df, on="master_metadata_track_name", how="outer")
    tracks_df["isInPlaylist"].fillna(0, inplace=True)
    tracks_df["counts"].fillna(0, inplace=True)
    tracks_df.to_csv("tracks.csv")

    return tracks_df