import pprint
from utils import convertToMin, _build


class User:
    def __init__(self, username):
        self.username = username

    def name(self, spotify):
        user = spotify.current_user()
        display_name = user['display_name']
        print(display_name)

    def albums(self, spotify, limit):
        '''
        outputs artist's name, album name, total tracks, 
        release date
        '''
        data = spotify.current_user_saved_albums(limit=50)['items']
        names = [attr['album']['artists'][0]['name'] for attr in data]
        album = [attr['album']['name'] for attr in data]
        total_tracks = [attr['album']['total_tracks'] for attr in data]
        release_date = [attr['album']['release_date'] for attr in data]
        albums = _build(names, album, total_tracks, release_date)

        print('Artist'.ljust(30), 'Album'.ljust(50), 'Release Date'.ljust(15), 'Track Numbers')
        for i in range(len(albums)):
            print(f'{albums[i][0].ljust(30)} {albums[i][1].ljust(50)} {albums[i][3].ljust(15)} {str(albums[i][2]).rjust(6)}')

    def tracks(self, spotify, limit):
        '''
        outputs track name, album name, track number, 
        duration, release date
        '''
        data = spotify.current_user_saved_tracks(limit=20)['items']
        track_name = [attr['track']['name'] for attr in data]
        track_number = [attr['track']['track_number'] for attr in data]
        duration = [convertToMin(attr['track']['duration_ms']) for attr in data]
        album_name = [attr['track']['album']['name'] for attr in data]
        release_date = [attr['track']['album']['release_date'] for attr in data] 

        tracks = _build(track_name, album_name, track_number, duration, release_date)
        print('Title'.ljust(25), 'Album'.ljust(25), 'Duration'.ljust(10), 'Track Numbers'.rjust(5), 'Release Date'.rjust(15))
        for i in range(len(tracks)):
            print(f'{tracks[i][0].ljust(25)} {tracks[i][1].ljust(25)} {tracks[i][3].ljust(10)} {str(tracks[i][2]).rjust(6)} {tracks[i][4].rjust(20)}')

    def playlists(self, spotify):
        '''
        outputs current user's playlists
        '''
        pass

    def saveAlbum(self, spotify, album_id):
        '''
        adds album to saved albums
        '''
        albums = [album_id]
        return spotify.current_user_saved_albums_add(albums=albums)

    def saveTracks(self, spotify):
        pass

    def __repr__(self):
        return f'User: {self.username} | Methods: .tracks(), .albums() .name()'