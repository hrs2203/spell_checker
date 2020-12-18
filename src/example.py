"""
Example on how to use query check class
"""

from query import QueryCheck

if __name__ == "__main__":
    queryChecker = QueryCheck("distance of sun from eart")

    # List of all word corrections
    print("====== Correction Word wise =================")
    wordCorrections = queryChecker.getCorrectedWords()
    for wordObj in wordCorrections:
        print(wordObj)
    print("=============================================")

    # List of all possible query
    print("====== Possible Query ( depth = 3 ) ==========")
    possibleQuery = queryChecker.getPossibleQuery(10)
    for queries in possibleQuery:
        print(queries)
    print("=============================================")
