import os
import suggest


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
        self.correctWord = [
            item for item in suggest.edits1(self.word) if self.isCorrect
        ]

    def setCorrectWord(self):
        if not self.isCorrect:
            self.correctWord = self.suggestionList(self.word)
        else:
            self.correctWord = [self.word]

    def __str__(self):
        prt = ""
        prt = f"{self.word} ->"
        for item in self.correctWord:
            prt = f"{prt} {item},"

        return prt

    def isSpelledCorrect(self, word: str) -> bool:
        """Checks wether it is a spelling mistake or not

        Args:
            word (str): word To Check

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
                flag = line[:-1] == word
                if flag:
                    break

            fileObj.close()
        except:
            flag = False

        # ======================

        return flag

    def suggestionList(self, word: str) -> list:
        """List of possible correct words

        Args:
            word (str): wrong input word

        Returns:
            list: List of possible correct words
        """

        correctSuggestionList = list()

        ## ======= suggestions  =======

        ## ======================

        return correctSuggestionList
