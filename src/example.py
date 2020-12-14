from query import QueryCheck

if __name__ == "__main__":
    queryChecker = QueryCheck("this is bood damr eaeth")

    # List of all word corrections
    print("====== Correction Word wise =====")
    wordCorrections = queryChecker.getCorrectedWords()
    for wordObj in wordCorrections:
        print(wordObj)
    print("=================================")
    
    # List of all possible query
    print("====== Possible Query ==========")
    possibleQuery = queryChecker.getPossibleQuery()
    for queries in possibleQuery:
        print(queries)
    print("=================================")
    