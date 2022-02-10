import spotipy
import sys
import webbrowser
from spotipy.oauth2 import SpotifyClientCredentials



uri = "3uwAm6vQy7kWPS2bciKWx9"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(uri, album_type='single')
albums = results['items']
done = []
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    found = False
    for i in done:
        if(i == album['name']):
            found = True
    if(found == False):
        print(album['name'])
        done.append(album['name'])

