from util import *
import texttable as tt


def takeInput():
    """Takes Input from user"""

    userInput = list(str(input("Enter your string: ")).split(" "))

    wordList = [Word(word) for word in userInput]

    printUserEntry(wordList)


def printUserEntry(wordList: list):
    """print Entry by user in table

    Args:
        wordList (list): List of word object
    """
    table = tt.Texttable()
    table.header(["Word", "isCorrect","suggestList"])
    words = []
    isCorrect = []
    suggestList = []

    for obj in wordList:
        words.append(obj.word)
        isCorrect.append(str(obj.isCorrect))
        suggestList.append(obj.correctWord)

    for row in zip(words, isCorrect, suggestList):
        table.add_row(row)

    tab = table.draw()
    print(tab)

