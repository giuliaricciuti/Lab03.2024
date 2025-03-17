import datetime
import time

import multiDictionary as md


class SpellChecker:

    def __init__(self):
        self.multid = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn.lower())
        errate = []
        parole = []

        print(f"-----------------"
              f"classica"
              f"-----------------")
        tic = datetime.datetime.now()
        parole = self.multid.searchWord(txtIn, language)
        errate = [w for w in parole if not w.corretta]
        l = len(errate)
        str=""
        for e in errate[:l-1]:
            str+= (f"{e.__str__()}, ")
        str+=(errate[l-1].__str__())
        print(str)
        toc = datetime.datetime.now()

        print(f"ci hai messo {toc-tic} \n"
              f"-----------------"
              f"dicotomica"
              f"-----------------")
        tic = datetime.datetime.now()
        parole = self.multid.searchWordDichotomic(txtIn, language)
        errate = [w for w in parole if not w.corretta]
        l = len(errate)
        str = ""
        for e in errate[:l - 1]:
            str += (f"{e.__str__()}, ")
        str += (errate[l - 1].__str__())
        print(str)
        toc = datetime.datetime.now()
        print(f"ci hai messo {toc - tic} \n")


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n" +
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`'*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text