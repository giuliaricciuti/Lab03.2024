
import dictionary as d
import richWord as rw



class MultiDictionary:

    def __init__(self):
        self.english = d.Dictionary("inglese", [])
        self.italian = d.Dictionary("italiano", [])
        self.spanish = d.Dictionary("spagnolo",[])

        self.english.loadDictionary("resources/English.txt")
        self.italian.loadDictionary("resources/Italian.txt")
        self.spanish.loadDictionary("resources/Spanish.txt")


    def printDic(self, language):
        if language == "english":
            print(self.english)
        elif language == "italian":
            print(self.italian)
        elif language == "spanish":
            print(self.spanish)
        else:
            print("No such language")

    def searchWord(self, words, language):
        parole=[]
        for word in words.split():
            richW = rw.RichWord(word)
            richW.corretta = False
            if language == "english":
                if self.english.dict.__contains__(word):
                    richW.corretta=True

            if language == "italian":
                if self.italian.dict.__contains__(word):
                    richW.corretta=True

            if language == "spanish":
                 if self.spanish.dict.__contains__(word):
                    richW.corretta=True
            parole.append(richW)
        return parole

    def searchWordDichotomic (self, words, language):
        parole = []
        for word in words.split():
            richW = rw.RichWord(word)
            if language == "english":
                dizionario = self.english
                self.searchDicotomic(richW, dizionario.dict)

            if language == "italian":
                dizionario = self.italian
                self.searchDicotomic(richW, dizionario.dict)

            if language == "spanish":
                dizionario = self.spanish
                self.searchDicotomic(richW, dizionario.dict)
            parole.append(richW)
        return parole

    def searchDicotomic(self, richW, dizionario = []):
        l = int(len(dizionario)/2)
        i = l
        if richW.__str__()==dizionario[l]:
            richW.corretta= True
        elif richW.__str__()<dizionario[l]:
            for i in range(0,l):
                if richW.__str__()==dizionario[i]:
                    richW.corretta=True
                    break
        elif richW.__str__()>dizionario[l]:
            for i in range(l, len(dizionario)):
                if richW.__str__()==dizionario[i]:
                    richW.corretta=True
                    break
        else:
            richW.corretta=False

