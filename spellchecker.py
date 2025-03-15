import datetime
import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDic = md.MultiDictionary()
        pass

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn.lower())

        print("\n INIZIALE \n")
        tic = datetime.datetime.now()
        parole = self.multiDic.searchWord(txtIn, language)
        errate = [p for p in parole if not p.corretta]
        toc = datetime.datetime.now()
        print (f"ci hai impiegato {toc-tic}")
        print ([e.__str__() for e in errate])

        print("\n LINEARE \n")
        parole = self.multiDic.searchWordLinear(txtIn, language)
        errate = [p for p in parole if not p.corretta]
        print([e.__str__() for e in errate])

        print("\n DICOTOMICA \n")
        parole = self.multiDic.searchWordDichotomic(txtIn, language)
        errate = [p for p in parole if not p.corretta]
        print([e.__str__() for e in errate])

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
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