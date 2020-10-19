import os, util

def suggestWordList(word: str) -> list:
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
    """Finds List of words in db with edit distance 1 and 2

    Args:
        word (str): word to search on

    Returns:
        list: list of possible words
    """
    tempWordList = []

    suggestionWordList_1 = suggestWordList(word)
    notTempWordList_1 = []
    tempWordList_1 = set([ word for word in suggestionWordList_1 if util.isPresent(word) ])
    notTempWordList_1 = [ word for word in suggestionWordList_1 if word not in tempWordList_1 ]
    tempWordList_1 = list(tempWordList_1)
    tempWordList.extend(tempWordList_1)
    tempWordList = list(set(tempWordList))

    ## TODO: takes to much time, so stopped for now
    if ( len(tempWordList) < ( len(word)//2 ) ):
        tempWordList_2 = []
        for tempWord in notTempWordList_1:
            tempWordList_2.extend( suggestWordList(tempWord) )
        tempWordList_2 = [ word for word in tempWordList_2 if util.isPresent(word) ]
        tempWordList.extend(tempWordList_2)
        tempWordList = list(set(tempWordList))

    countWordList = [ [word, util.getWordCount(word)] for word in tempWordList ]
    countWordList.sort(key=lambda item: item[1], reverse=True)
    wordList = [ word[0] for word in countWordList ]
    return wordList

