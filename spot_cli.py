import os
import pprint
import sys
import datetime
import time
from subprocess import call
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
from search import search
from classes.User import User


def generateToken(username):
    '''
    generates auth token for spotify object
    '''
    try:
        token = util.prompt_for_user_token(
            username, scope="user-library-read playlist-modify-private user-library-modify")
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(
            username, scope="user-library-read playlist-modify-private user-library-modify")
    return token

def listAlbum(spotify, artist_name):
    '''
    lists albums & album id
    '''
    artist_id = searchArtist(artist_name)[1]
    artist_albums = artistAlbums(artist_id, limit=50)
    for selection in artist_albums:
        name, album_id = selection
        print(name.ljust(50), album_id.ljust(50))

# TODO
def songDetails(songs):
    '''
    get details of specific song
    '''
    pass

def commands(arg, user, spotify):
    '''
    command line arguments
    '''
    if arg == '-t':
        user.tracks(spotify, limit=10)
    elif arg == '-a':
        user.albums(spotify, limit=10)
    elif arg == '-s':
        search(spotify)
    elif arg == '-la':
        artist = sys.argv[-1]
        listAlbum(spotify, artist)
    elif arg == '-sa':
        album_id = sys.argv[-1]
        user.saveAlbum(spotify, album_id)
    else:
        print('Enter a valid command')

if __name__ == "__main__":
    if len(sys.argv) == 1:
        call(["python", "menu.py", "-h"])
    elif len(sys.argv) >= 3:
        username = sys.argv[1]
        command = sys.argv[2]
        token = generateToken(username)
        spotify = spotipy.Spotify(auth=token)
        user = User(username)
        commands(command, user, spotify)