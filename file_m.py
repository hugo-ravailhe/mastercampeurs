import ntpath

class file:
    def __int__(self, path):
        self.path = path
        self.name = ntpath.basename(path)