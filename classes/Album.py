class Album:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        for k in list(self.__dict__.keys()):
            self.k = kwargs.get(k)
        self.__initialize__()

    def __initialize__(self, *args):
        ''' 
        build individual track items 
        '''
        return list(zip(v for v in self.__dict__.values()))

    def __repr__(self):
        return f'{self.__dict__}'
