"""
Example on how to use query check class
"""

from query import QueryCheck

if __name__ == "__main__":
    queryChecker = QueryCheck("globad wareing")

    # List of all word corrections
    print("====== Correction Word wise =================")
    wordCorrections = queryChecker.getCorrectedWords()
    for wordObj in wordCorrections:
        print(wordObj)
    print("=============================================")

    # List of all possible query
    print("====== Possible Query ( depth = 3 ) ==========")
    possibleQuery = queryChecker.getPossibleQuery()
    for queries in possibleQuery:
        print(queries)
    print("=============================================")

    # List of all possible query
    print("====== Possible Query ( depth = 5 ) ==========")
    possibleQuery = queryChecker.getPossibleQuery(5)
    for queries in possibleQuery:
        print(queries)
    print("=============================================")
