import os
import pprint
import sys
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import requests


# username
username = sys.argv[1]
token = util.prompt_for_user_token(username)

try:
    token = util.prompt_for_user_token(username)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# create our spotify object
spotify = spotipy.Spotify(auth=token)
user = spotify.current_user()

display_name = user['display_name']
print('Current User: ', display_name)

def searchArtist(name, limit=10):
    '''
    return spotify page & artist id of queried artist
    '''
    url_temp = []
    id_temp = []

    search = spotify.search(q=name, type='artist')
    data = search['artists']

    # larger following is the actual artist aka the 1st choice
    for attr in data['items']:
        # print(attr['id'])
        id_temp.append(attr['id'])
        url_temp.append(attr['external_urls']['spotify'])

    # need artist id & url of artist
    return url_temp[0], id_temp[0]


def artistAlbums(artist_id):
    '''
    returns the albums & album id's of artist
    '''
    albums = []
    a = spotify.artist_albums(artist_id)
    data = a['items']

    # pprint.pprint(data)
    for attr in data:
        if attr['type'] == 'album':
            album_name, album_id = attr['name'], attr['id']
            albums.append((album_name, album_id))

    return albums


def getAlbumSongs(album_id):
    



if __name__ == "__main__":
    url, artist_id = searchArtist('dylvinci')
    print(artist_id)
    print(artistAlbums(artist_id))