from util import *

def takeInput():
    """Takes Input from user"""

    userInput = list( map( str, str(input("Enter your string: ")).split(" ") ) )
 
    wordList = [ Word(word) for word in userInput ]

    print("Entry by user")
    for obj in wordList:
        print(obj)
    







