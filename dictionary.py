class Dictionary:
    def __init__(self, linguaggio, dict=[]):
        self.linguaggio = linguaggio
        self._dict = dict
        pass

    def loadDictionary(self, path):
        file_path = path
        with open(file_path, 'r') as file:
            for line in file:
                value = line.strip()
                self._dict.append(value.lower())

    def printAll(self):
        for d in self._dict:
            print(d)

    @property
    def dict(self):
        return self._dict
