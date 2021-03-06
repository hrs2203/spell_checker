import os, suggest

def getWord(string: str) -> str:
    """Word from db word format

    Args:
        string (str): word fromat from db

    Returns:
        str: word
    """
    return string.split("=")[0]

def getCount(string: str) -> int:
    """Count of word in db

    Args:
        string (str): word

    Returns:
        int: count
    """
    try:
        return int(string.split("=")[1])
    except:
        return 0

def getNewWord(word: str) -> str:
    """new word that can be added to db

    Args:
        word (str): word to add

    Returns:
        str: db format
    """
    return f"{word}=1"

def incrementWordCount(string: str) -> str:
    """incremenent word count in db format

    Args:
        string (str): word

    Returns:
        [str]: string
    """
    temp = string.split("=")
    count = int(temp[1])+1
    return f"{temp[0]}={count}"

def getFileName(word: str) -> str:
    if (len(word)==1):
        startChar = word[0].lower()
        return f"{startChar}.txt"
    
    if (word[1]<'i'):
        startChar = word[0].lower()
    elif (word[1]>='i' and word[1]<'r'):
        startChar = f"{word[0].lower()}i"
    else:
        startChar = f"{word[0].lower()}r"
    return f"{startChar}.txt"


def isPresent(word: str ) -> bool:
    """Checks wether it is a spelling mistake or not

    Returns:
        bool: (is_correct_word) ? true : false;
    """
    flag = False
    BASE_DIR = os.getcwd()
    RESULT_DATA_PATH = os.path.join(BASE_DIR, "data", "search_data")
    # ======= check  =======
    fileHead = getFileName(word)
    fileName = os.path.join(RESULT_DATA_PATH, fileHead)

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

def getWordCount(word):
    flag = False
    count = 0
    BASE_DIR = os.getcwd()
    RESULT_DATA_PATH = os.path.join(BASE_DIR, "data", "search_data")
    # ======= check  =======
    fileHead = getFileName(word)
    fileName = os.path.join(RESULT_DATA_PATH, fileHead)
    try:
        fileObj = open(fileName, "r")

        for line in fileObj:
            flag = (getWord(line[:-1]) == word)
            count = getCount(line[:-1])
            if flag:
                break

        fileObj.close()
    except:
        flag = False
        count = 0

    # ======================

    return count

class Word:
    """Word Class"""

    word = ""
    isCorrect = False
    correctWord = []
    BASE_DIR = os.getcwd()
    RESULT_DATA_PATH = os.path.join(BASE_DIR, "data", "search_data")

    def __init__(self, word: str):
        self.word = word
        self.isCorrect = isPresent(self.word)
        self.setCorrectWord()

    def __str__(self):
        prt = ""
        prt = f"{self.word} ->"
        for item in self.correctWord:
            prt = f"{prt} {item},"

        return prt

    def setCorrectWord(self):
        # print(f"working on {self.word}... ", end=" ")
        try:
            if not self.isCorrect:
                self.correctWord = suggest.suggestionList(self.word)
            else:
                self.correctWord = []
            # print("Done")
        except expression as identifier:
            self.correctWord = []
            # print("Error")
        
        

