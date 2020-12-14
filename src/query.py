from util import *


class QueryCheck:
    """Query Input"""

    wordList = list()
    initQuery = ""

    def __init__(self, queryInput: str = ""):
        self.initQuery = queryInput
        self.wordList = [Word(word) for word in queryInput.split(" ")]

    def getCorrectedWords(self) -> list:
        """List of Object (Word) for all corrected word

        Returns:
            list: List of correct word objects
        """
        responseList = [word for word in self.wordList if not word.isCorrect]
        return responseList

    def getPossibleQuery(self) -> list:
        """List of possible query after correction

        Returns:
            list: List of query
        """
        responseList = list()

        # ======= query creation ========

        


        # ===============================

        responseList.append(self.initQuery)
        return responseList
