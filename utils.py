import datetime


def convertToMin(ms):
    '''
    converts milliseconds to minutes
    '''
    time = datetime.timedelta(milliseconds=ms)
    return str(time)[:-7]

def outputAlbum(a):
    print('Artist'.ljust(30), 'Album'.ljust(50),
          'Release Date'.ljust(15), 'Track Numbers')
    for i in range(len(a.names)):
        print(f'{a.names[i].ljust(30)} {a.album[i].ljust(50)} {str(a.release_date[i]).ljust(15)} {str(a.total_tracks[i]).rjust(6)}')

def outputTrack(t):
    print('Title'.ljust(25), 'Album'.ljust(25), 'Duration'.ljust(10), 'Track Numbers'.rjust(5), 'Release Date'.rjust(15))
    for i in range(len(t.track_name)):
        print(f'{t.track_name[i].ljust(25)} {t.album_name[i].ljust(25)} {str(t.duration[i]).ljust(10)} {str(t.track_number[i]).rjust(6)} {t.release_date[i].rjust(20)}')

def outputSlots(a):
    album_slots = []
    print('Slot'.ljust(15), 'Artist'.ljust(30), 'Album'.ljust(50),
        'Release Date'.ljust(15), 'Track Numbers')
    for i in range(len(a)):
        album_slots.append(i)
        print(str(i).ljust(15), a[i][0].ljust(30), a[i][1].ljust(50), a[i][3].ljust(15), a[i][4])
    return album_slots

def outputAlbumTracks(songs, artist, album_name):
    print(f'\n{artist} - {album_name}\'s Tracklist: \n')
    print('Track Name'.ljust(30), 'Duration'.ljust(30), 'Track Numbers')
    for name, duration, number in songs:
        print(name.ljust(30), str(duration).ljust(30), str(number).ljust(15))