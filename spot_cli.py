import os
import pprint
import sys
import datetime
from subprocess import call
from classes import User
from utils import convertToMin
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

def generateToken(username):
    '''
    generates auth token for spotify object
    '''
    try:
        token = util.prompt_for_user_token(username, scope="user-library-read playlist-modify-private")
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope="user-library-read playlist-modify-private")
    return token

def searchArtist(name, limit=10):
    '''
    return artist spotify url & artist id
    '''
    artist = []
    search = spotify.search(q=name, type='artist')
    data = search['artists']
    for attr in data['items']:
        artist.append((attr['id'], attr['external_urls']['spotify']))
    return artist[0][1], artist[0][0]

def artistAlbums(artist_id):
    '''
    returns the albums & albums' id of artist
    '''
    albums = []
    a = spotify.artist_albums(artist_id)
    data = a['items']
    for attr in data:
        if attr['type'] == 'album':
            album_name, album_id = attr['name'], attr['id']
            albums.append((album_name, album_id))
    return albums

def getAlbumSongs(album_id):
    '''
    returns tracks array of specific album
    track consists of track name, track number, track duration
    '''
    tracks = []
    a_tracks = spotify.album_tracks(album_id)
    data = a_tracks['items']
    # pprint.pprint(data)
    for attr in data:
        track_name, track_number, duration = attr['name'], attr['track_number'], convertToMin(attr['duration_ms'])
        tracks.append((track_number, track_name, duration))
    return tracks

def printAlbums(artist, artist_id):
    ''' 
    prints albums of artist 
    '''
    albums = artistAlbums(artist_id)
    album_slots = []
    print(f'{artist}\'s Discography: ')
    for i in range(len(albums)):
        album_slots.append(i)
        print(i, albums[i][0])
    return album_slots, albums

def printTracksOfAlbum(artist, album_slots, albums):
    '''
    prints tracks of album
    '''
    album_number_response = int(input('Type in the # of the album you would like to browse: (press any key to esc) '))
    if album_number_response in album_slots:
        album_name, album_id = albums[album_number_response][0], albums[album_number_response][1]
        songs = getAlbumSongs(album_id)
        print(f'\n{artist} - {album_name}\'s Tracklist: ')
        for track_number, track_name, duration in songs:
            print(track_number, track_name, duration)
    else:
        sys.exit()
    return songs

def songDetails(songs):
    '''
    get details of specific song
    '''
    pass

def search():
    '''
    search loop
    '''
    artist = input('Enter the artist to search for: ')
    url, artist_id = searchArtist(artist)
    album_slots, albums = printAlbums(artist, artist_id)
    print('\n')
    songs = printTracksOfAlbum(artist, album_slots, albums)


def commands(arg, user, spotify):
    '''
    command line arguments
    '''
    if arg == '-t':
        user.tracks(spotify, limit=10)    
    elif arg == '-a':
        user.albums(spotify, limit=10)
    elif arg == '-s':
        search()
    else:
        print('Enter a valid command')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        call(["python", "menu.py", "-h"])

    elif len(sys.argv) == 3:
        username = sys.argv[1]
        command = sys.argv[2]
        token = generateToken(username)
        spotify = spotipy.Spotify(auth=token)

        user = User(username)
        commands(command, user, spotify)