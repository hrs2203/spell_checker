import os

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
            flag = line[:-1] == word
            if flag:
                break

        fileObj.close()
    except:
        flag = False

    # ======================

    return flag

def edit_dist_1(word: str) -> list:
    """All edits that are one edit away from `word`.

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
    return set(deletes + transposes + replaces + inserts)


def edit_dist_2(word):
    """All edits that are two edit away from `word`.

    Args:
        word (str): word to work on

    Returns:
        list: possible words
    """
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

def suggestionList(word: str) -> list:
    tempWordList = list(edit_dist_1(word))
    wordList = [ word for word in tempWordList if isPresent(word) ]
    return wordList