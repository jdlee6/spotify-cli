from main import search

def commands(arg, user, spotify):
    if arg == 't':
        user.tracks(spotify, limit=20)    

    elif arg == 'a':
        user.albums(spotify, limit=20)

    elif arg == 's':
        search()