import os

import dictionary
import dictionary as d
import richWord as rw



class MultiDictionary:
    def __init__(self):
        self.english = d.Dictionary([], 'english')
        self.italian = d.Dictionary([], 'italian')
        self.spanish = d.Dictionary([], 'spanish')

        self.english.loadDictionary("resources/English.txt")
        self.italian.loadDictionary("resources/Italian.txt")
        self.spanish.loadDictionary("resources/Spanish.txt")
        pass


    def printDic(self, language):
        if language == "english":
            print(self.english)
        elif language == "italian":
            print(self.italian)
        elif language == "spanish":
            print(self.spanish)
        else:
            print("Language not recognized")


    def searchWord(self, words, language):
        parole = []
        for word in words.split():
            trovata = False
            richw = rw.RichWord(word)
            if language == "english" and word in self.english.dict:
                trovata = True
            elif language == "italian" and word in self.italian.dict:
                trovata = True
            elif language == "spanish" and word in self.spanish.dict:
                trovata = True
            if trovata:
                richw.corretta = True
            parole.append(richw)
        return (parole)

    def searchWordLinear(self, words, language):
        parole = []
        for word in words.split():
            richw = rw.RichWord(word)
            if language == "english":
                w = next((p for p in self.english.dict if p==word), None)
            elif language == "italian":
                w = next((p for p in self.italian.dict if p == word), None)
            elif language == "spanish":
                w = next((p for p in self.spanish.dict if p == word), None)
            if w != None:
                richw.corretta = True
            parole.append(richw)
        return (parole)

    def searchWordDichotomic(self, words, language):
        parole = []
        for word in words.split():
            richw = rw.RichWord(word)
            if language == "english":
                dict = self.english.dict
                richw.corretta = searchDicotomic(word, dict)
            elif language == "italian":
                dict = self.italian.dict
                richw.corretta = searchDicotomic(word, dict)
            elif language == "spanish":
                dict = self.spanish.dict
                richw.corretta = searchDicotomic(word, dict)
            parole.append(richw)
        return (parole)

def searchDicotomic(word, dict):
    len = len(dict)
    if word == dict(len/2):
        return True
    elif word > dict(len/2):
        pass

