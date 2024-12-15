import streamlit as st
import json
import pandas as pd
import plotly.express as px
import numpy as np

# Sidebar

# Main content
st.title('XXX')
st.markdown(
    """
    XXX
    """
)

# Upload data
with open('data_extended_streaming\Streaming_History_Audio_2022-2024_1.json') as f1:
    data1 = json.load(f1)
with open('data_extended_streaming\Streaming_History_Audio_2018-2022_0.json') as f2:
    data2 = json.load(f2)

# Manipulate dataframe
df1 = pd.DataFrame.from_dict(data1, orient='columns')
df2 = pd.DataFrame.from_dict(data2, orient='columns')
df = pd.concat([df1, df2], axis=0) 
df = df.drop(['ip_addr','spotify_track_uri','platform','offline_timestamp','incognito_mode','spotify_episode_uri'], axis=1)
df['ts'] = pd.to_datetime(df['ts'])
df['date'] = pd.to_datetime(df['ts']).dt.date
df['time'] = pd.to_datetime(df['ts']).dt.time
df['year'] = pd.to_datetime(df['ts']).dt.year
df['s_played'] = df["ms_played"]/1000

artists = df.groupby(["year","master_metadata_album_artist_name"]).sum('ms_played')
artists.reset_index(drop=False, inplace=True)

year_list = [2024,2023,2022,2021,2020,2019]


yr19 = artists[artists["year"]==2019]
max19 = yr19.loc[yr19['ms_played'].idxmax()]['master_metadata_album_artist_name']

yr20 = artists[artists["year"]==2020]
max20 = yr20.loc[yr20['ms_played'].idxmax()]['master_metadata_album_artist_name']

yr21 = artists[artists["year"]==2021]
max21 = yr21.loc[yr21['ms_played'].idxmax()]['master_metadata_album_artist_name']

yr22 = artists[artists["year"]==2022]
max22 = yr22.loc[yr22['ms_played'].idxmax()]['master_metadata_album_artist_name']

yr23 = artists[artists["year"]==2023]
max23 = yr23.loc[yr23['ms_played'].idxmax()]['master_metadata_album_artist_name']

yr24 = artists[artists["year"]==2024]
max24 = yr24.loc[yr24['ms_played'].idxmax()]['master_metadata_album_artist_name']

artist_set = set([max19,max20,max21,max22,max23,max24])
artist_list = list(artist_set)

chart_type = st.radio('Choose an artist:', [artist_list])