Running this project is done solely from the SpotifyReport.ipynb Jupyter Notebook.
Some of the longer tasks (cleaning, joining of tables) are moved over to a utils.py file to avoid clogging up the Notebook.
The raw Spotify listening history, as it came to me, is in endsong_0.json and endsong_1.json.
endsong.json is simply the two other JSON files combined into one, to make things easier.
playlist.csv is the CSV I made by hand which I join with part of the Spotify data to make the main table I use in this project.
tracks.csv is created from code within the Jupyter Notebook, and contains the aforementioned main table.