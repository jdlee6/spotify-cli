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