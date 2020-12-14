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

    def getPossibleQuery(self, depth: int = 3) -> list:
        """List of possible query after correction

        Args:
            depth (int, optional): How many correction per word needed. Defaults to 3.

        Returns:
            list: List of query
        """
        responseList = list()
        responseList.append(self.initQuery)

        wordCorrectionList = self.getCorrectedWords()

        # ======= query creation ========

        for word in wordCorrectionList:
            tempCorrection = word.correctWord[:depth]
            tempWord = word.word
            queryCount = len(responseList)
            correctionCount = len(tempCorrection)

            for query in range(queryCount):
                tempQuery = responseList[0].split(" ")
                tempWordIndex = tempQuery.index(tempWord)
                responseList = responseList[1:]

                tempQueryCorrection = list()
                for correctionIndex in range(correctionCount):
                    tempQueryCorrection = tempQuery.copy()
                    tempQueryCorrection[tempWordIndex] = tempCorrection[correctionIndex]
                    tempQueryCorrection = " ".join(tempQueryCorrection)
                    responseList.append(tempQueryCorrection)

        # ===============================

        responseList.append(self.initQuery)
        return responseList
