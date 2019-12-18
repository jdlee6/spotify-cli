from classes.Album import Album
from classes.Track import Track
from utils import outputAlbum, outputSlots, outputTrack, convertToMin, outputAlbumTracks
import itertools
import sys


def searchArtist(name, spotify, limit=10):
    '''
    return artist spotify url & artist id
    '''
    if name == '':
        sys.exit()
    artist = []
    search = spotify.search(q=name, type='artist')
    data = search['artists']
    for attr in data['items']:
        artist.append((attr['id'], attr['external_urls']['spotify']))
    return name, artist[0][1], artist[0][0]

def artistAlbums(artist, artist_id, spotify):
    '''
    returns the albums & albums' id of artist
    '''
    albums = []
    data = spotify.artist_albums(artist_id, limit=10)['items']
    a = Album(names=[artist],
            album=[attr['name'] for attr in data],
                id = [attr['id'] for attr in data],
                release_date=[attr['release_date'] for attr in data],
                total_tracks=[attr['total_tracks'] for attr in data]
                )
    # zip_longest is for zipping iterables with uneven lengths
    albums = list(itertools.zip_longest(a.names, a.album, a.id, a.release_date, a.total_tracks, fillvalue=artist))
    return albums

def slotAlbums(artist, artist_id, spotify):
    '''
    prints the slots of albums
    '''
    albums = artistAlbums(artist, artist_id, spotify)
    return outputSlots(albums), albums

def albumSongs(album_id, spotify):
    '''
    returns tracks array of specific album
    track consists of track name, track number, track duration
    '''
    data = spotify.album_tracks(album_id)['items']
    t = Track(name=[attr['name'] for attr in data],
                duration=[convertToMin(attr['duration_ms']) for attr in data],
                number=[attr['track_number'] for attr in data])
    songs = list(zip(t.name, t.duration, t.number))
    return songs

def printTracksOfAlbum(artist, album_slots, albums, spotify):
    '''
    prints tracks of album
    '''
    album_number_response = int(input(
        'Type in the # of the album you would like to browse: (press any key to esc) '))
    if album_number_response in album_slots:
        album_name, album_id = albums[album_number_response][0], albums[album_number_response][2]
        songs = albumSongs(album_id, spotify)
        outputAlbumTracks(songs, artist, album_name)
    else:
        sys.exit()
    return songs

def search(spotify):
    '''
    search loop
    '''
    artist = input('Enter the artist to search for: ')
    name, url, artist_id = searchArtist(artist, spotify)
    album_slots, albums = slotAlbums(artist, artist_id, spotify)
    print('\n')
    songs = printTracksOfAlbum(artist, album_slots, albums, spotify)

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