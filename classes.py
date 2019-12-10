import pprint

class User:
    def __init__(self, username):
        self.username = username

    def name(self, spotify):
        '''
        name of current_user
        '''
        user = spotify.current_user()
        display_name = user['display_name']
        print(display_name)

    def albums(self, username, spotify, limit):
        '''
        returns current user's saved albums
        '''
        data = spotify.current_user_saved_albums(limit=limit)
        for attr in data['items']:
            name = attr['album']['artists'][0]['name']
            album = attr['album']['name']
            total_tracks = attr['album']['total_tracks']
            release_date = attr['album']['release_date']

            print(name, album, total_tracks, release_date)

    def playlists(self, spotify):
        pass


    def __repr__(self):
        return f'User: {self.username}'