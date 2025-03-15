
class Dictionary:
    def __init__(self, _dict=[], language =''):
        self._dict = _dict
        self.language = language
        pass

    def loadDictionary(self, path):
        file_path = path
        with open(file_path, 'r') as file:
            for line in file:
                self._dict.append(line.strip().lower())
        pass


    def printAll(self):
        print(self._dict)
        pass


    @property
    def dict(self):
        return self._dict
