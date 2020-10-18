import os

def getWord(string):
    return string.split("=")[0]

def getCount(string):
    try:
        return int(string.split("=")[1])
    except:
        return 0

def getWordCount(word):
    flag = False
    count = 0
    BASE_DIR = os.getcwd()
    RESULT_DATA_PATH = os.path.join(BASE_DIR, "data", "search_data")
    # ======= check  =======
    startChar = word[0].lower()
    fileName = os.path.join(RESULT_DATA_PATH, f"{startChar}.txt")
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

def getNewWord(word):
    return f"{word}=0"

def incrementWordCount(string):
    temp = string.split("=")
    count = int(temp[1])+1
    return f"{temp[0]}={count}"

def isPresent(word: str) -> bool:
    """Checks wether it is a spelling is present in db or not

    Returns:
        bool: (is_present) ? true : false;
    """
    flag = False
    BASE_DIR = os.getcwd()
    RESULT_DATA_PATH = os.path.join(BASE_DIR, "data", "search_data")
    # ======= check  =======
    startChar = word[0].lower()
    fileName = os.path.join(RESULT_DATA_PATH, f"{startChar}.txt")
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

def edit_dist_1(word: str) -> list:
    """All edits that are one edit away from `word`.
    
    source: http://norvig.com/spell-correct.html

    Args:
        word (str): word to work on

    Returns:
        list: possible words
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return list(set(deletes + transposes + replaces + inserts))


def suggestionList(word: str) -> list:
    tempWordList = edit_dist_1(word)
    countWordList = [ [word, getWordCount(word)] for word in tempWordList if isPresent(word) ]
    countWordList.sort(key=lambda item: item[1], reverse=True)
    wordList = [ word[0] for word in countWordList ]
    return wordList