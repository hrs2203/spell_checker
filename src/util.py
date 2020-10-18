import os, suggest

def getWord(string):
    return string.split("=")[0]

def getCount(string):
    try:
        return int(string.split("=")[1])
    except:
        return 0

def getNewWord(word):
    return f"{word}=0"

def incrementWordCount(string):
    temp = string.split("=")
    count = int(temp[1])+1
    return f"{temp[0]}={count}"

class Word:
    """Word Class"""

    word = ""
    isCorrect = False
    correctWord = []
    BASE_DIR = os.getcwd()
    RESULT_DATA_PATH = os.path.join(BASE_DIR, "data", "search_data")

    def __init__(self, word: str):
        self.word = word
        self.isCorrect = self.isSpelledCorrect(self.word)
        self.setCorrectWord()

    def __str__(self):
        prt = ""
        prt = f"{self.word} ->"
        for item in self.correctWord:
            prt = f"{prt} {item},"

        return prt

    def setCorrectWord(self):
        if not self.isCorrect:
            self.correctWord = suggest.suggestionList(self.word)
        else:
            self.correctWord = []

    def isSpelledCorrect(self, word: str ) -> bool:
        """Checks wether it is a spelling mistake or not

        Returns:
            bool: (is_correct_word) ? true : false;
        """
        flag = False
        # ======= check  =======
        startChar = word[0].lower()
        fileName = os.path.join(self.RESULT_DATA_PATH, f"{startChar}.txt")

        try:
            fileObj = open(fileName, "r")

            for line in fileObj:
                flag = (getWord(line[:-1]) == word)
                if flag:
                    break

            fileObj.close()
        except:
            flag = False

        # ======================

        return flag
