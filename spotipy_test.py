import spotipy
import sys
import os
from dotenv import load_dotenv

from pathlib import Path

dotenv_path = Path('path/to/.env')

load_dotenv(dotenv_path=dotenv_path)

SPOTIFY_CLIENT_ID=os.getenv('SPOTIPY_CLIENT_ID')



print(SPOTIFY_CLIENT_ID)
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
