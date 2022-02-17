from __future__ import print_function
import sys
import spotipy
import spotipy.util as util
from dotenv import load_dotenv

load_dotenv()


scope = 'user-read-playback-state user-modify-playback-state'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    d = sp.devices()
    print(d)
    for i in d['devices']:
        print(i)
        if i['is_active']:
            print(i['name'] + "ACTIVE")

sp.next_track()
