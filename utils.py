import datetime


def convertToMin(ms):
    '''
    converts milliseconds to minutes
    '''
    time = datetime.timedelta(milliseconds=ms)
    return str(time)[:-7]

def _build(*args):
    '''
    param: iterables
    '''
    return list(zip(*args))
