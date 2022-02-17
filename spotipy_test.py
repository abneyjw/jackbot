import spotipy,sys,time
import webbrowser
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

spotify.next_track()

name = input()


results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    results = spotify.artist_top_tracks(artist['uri'])
    count = 0
    for track in results['tracks'][:10]:
        count += 1;
        print('track {}'.format(count) + ':' + track['name'])
    print(artist['name'], artist['images'][0]['url'])

spotify.next_track()
    
    

#webbrowser.open(artist['images'][0]['url'])
