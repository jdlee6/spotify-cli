import pprint
from utils import convertToMin, outputAlbum, outputTrack
from classes.Track import Track
from classes.Album import Album


class User:
    def __init__(self, username):
        self.username = username

    def name(self, spotify):
        user = spotify.current_user()
        return user['display_name']

    def albums(self, spotify, limit):
        '''
        outputs artist's name, album name, total tracks, 
        release date
        '''
        data = spotify.current_user_saved_albums(limit=50)['items']
        a = Album(names=[attr['album']['artists'][0]['name'] for attr in data],
                  album=[attr['album']['name'] for attr in data],
                  total_tracks=[attr['album']['total_tracks']
                                for attr in data],
                  release_date=[attr['album']['release_date'] for attr in data])
        return outputAlbum(a)

    def tracks(self, spotify, limit):
        '''
        outputs track name, album name, track number, 
        duration, release date
        '''
        data = spotify.current_user_saved_tracks(limit=20)['items']
        t = Track(
            track_name=[attr['track']['name'] for attr in data],
            track_number=[attr['track']['track_number'] for attr in data],
            duration=[convertToMin(attr['track']['duration_ms'])
                      for attr in data],
            album_name=[attr['track']['album']['name'] for attr in data],
            release_date=[attr['track']['album']['release_date']
                          for attr in data]
        )
        return outputTrack(t)

    def saveAlbum(self, spotify, album_id):
        '''
        adds album to saved albums
        '''
        albums = [album_id]
        return spotify.current_user_saved_albums_add(albums=albums)

    def saveTracks(self, spotify):
        pass

    def playlists(self, spotify):
        '''
        outputs current user's playlists
        '''
        pass

    def __repr__(self):
        return f'User: {self.username} | Methods: .tracks(), .albums() .name() .saveAlbum()'
