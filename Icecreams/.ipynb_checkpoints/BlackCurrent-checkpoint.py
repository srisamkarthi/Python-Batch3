class BlackCurrent:
    def __init__(self):
        self.flavours = ['cake', 'vanilla', 'chocolatee']
        print('init Black Current')
    def showFlavours(self):
        print('These are the available Flavours in Black Current')
        for flavour in self.flavours:
            print('\t%s ' % flavour)