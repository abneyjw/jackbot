from __future__ import print_function
import sys
import time
import spotipy
import spotipy.util as util
import urllib.request
from dotenv import load_dotenv

class Spotify:
    load_dotenv()

    def current(self):
        return ("Currently Playing: " + sp.currently_playing()['item']['name'] + " - " + sp.currently_playing()['item']['artists'][0]['name'])

    def interact2(self, sp):
        loop = True
        print("Valid Commands: skip, prev, pause, play, current, quit")
        while(loop):
            cmd = input()
            try:
                if(cmd == "skip"):
                    sp.next_track()
                elif(cmd == "prev"):
                    sp.previous_track()
                elif(cmd == "pause"):
                    sp.pause_playback()
                elif(cmd == "play"):
                    sp.start_playback()
                elif(cmd == "current"):
                    return self.current()
                elif(cmd == "quit"):
                    loop = False
                else:
                    print("Valid Commands: skip, prev, pause, play, current, quit")
            except spotipy.SpotifyException as err:
                print(err)

    def interact(self,cmd):
        print(cmd)
        if(cmd == "skip"):
            sp.next_track()
        elif(cmd == "prev"):
            sp.previous_track()
        elif(cmd == "pause"):
            sp.pause_playback()
        elif(cmd == "play"):
            sp.start_playback()
        elif(cmd == "current"):
            self.current(sp)

    def setup(self):
        scope = 'user-read-playback-state user-modify-playback-state'


        username = "abneyjw"

        token = util.prompt_for_user_token(username, scope)
        found = False

        if token:
            global sp
            sp = spotipy.Spotify(auth=token)
            for i in range(5):
                d = sp.devices()
                print("[ATTEMPT "+str(i+1)+"] Searching for active device"),
                time.sleep(1)
                print('.'),
                time.sleep(1)
                print('.'),
                time.sleep(1)
                print('.')
                for j in d['devices']:
                    if j['is_active']:
                        found = True
                        print(j['name'] + " is active.")
                        break
                if(found):
                    break

            