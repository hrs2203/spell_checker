import os, util

charSet = [
    "a",
    "ai",
    "ar",
    "b",
    "bi",
    "br",
    "c",
    "ci",
    "cr",
    "d",
    "di",
    "dr",
    "e",
    "ei",
    "er",
    "f",
    "fi",
    "fr",
    "g",
    "gi",
    "gr",
    "h",
    "hi",
    "hr",
    "i",
    "ii",
    "ir",
    "j",
    "ji",
    "jr",
    "k",
    "ki",
    "kr",
    "l",
    "li",
    "lr",
    "m",
    "mi",
    "mr",
    "n",
    "ni",
    "nr",
    "o",
    "oi",
    "or",
    "p",
    "pi",
    "pr",
    "q",
    "qi",
    "qr",
    "r",
    "ri",
    "rr",
    "s",
    "si",
    "sr",
    "t",
    "ti",
    "tr",
    "u",
    "ui",
    "ur",
    "v",
    "vi",
    "vr",
    "w",
    "wi",
    "wr",
    "x",
    "xi",
    "xr",
    "y",
    "yi",
    "yr",
    "z",
    "zi",
    "zr",
]


def train_data():
    BASE_DIR = os.getcwd()
    TRAINING_DATA_PATH = os.path.join(BASE_DIR, "data", "train_data_set")
    RESULT_DATA_PATH = os.path.join(BASE_DIR, "data", "search_data")

    print("=========== Deleting existing data set ===========")

    fileList = os.listdir(RESULT_DATA_PATH)
    for fileName in fileList:
        try:
            os.remove(os.path.join(RESULT_DATA_PATH, fileName))
        except:
            print(f"Some error while deleting {fileName}")

    print("=============== Deleted Finish ====================")

    print("=========== creating empty db set ===========")

    for letter in charSet:
        fileName = os.path.join(RESULT_DATA_PATH, f"{letter}.txt")
        open(fileName, "w").close()

    print("============== created set ==================")

    tempFileList = os.listdir(TRAINING_DATA_PATH)
    fileList = [os.path.join(TRAINING_DATA_PATH, fileName) for fileName in tempFileList]

    # for letter in charSet:
    #     fileName = os.path.join(RESULT_DATA_PATH, f"{letter}.txt")

    #     if not os.path.exists(fileName):
    #         open(fileName, "w").close()

    #     for trainFile in fileList:
    #         textList = readTrainingFile(trainFile, letter)
    #         for word in textList:
    #             writeWordToFile(fileName, word)
    #     print(f"{letter} done.")

    for train_file in fileList:
        fileContent = fileSplit(readTrainingFile(train_file))
        for charStart in fileContent:
            for wordSet in charStart:
                for word in wordSet:
                    fileName = os.path.join(RESULT_DATA_PATH, util.getFileName(word))
                    writeWordToFile(fileName, word)
        print(f"training done for file {train_file}")

    print("=============== training finished ==================")


def readTrainingFile(filePath: str) -> list:
    """Reads file and return unique word list
    starting with startChar

    Args:
        filePath (str): file to read path
        startChar (str): word starting char

    Returns:
        list: list of unique words starting with word
    """

    stopList = [".", ",", ":", ")", "(", "}", "{", "[", "]"]

    response = list()

    fileObj = open(filePath, "r")
    fileString = fileObj.read()

    # todo: need some work in pre processing
    # train after it's done
    for char in stopList:
        fileString = fileString.replace(char, " ")

    fileWord = fileString.split()
    fileWord = [word.lower() for word in fileWord]

    response = [[] for _ in range(26)]
    for word in fileWord:
        try:
            response[ord(word[0]) - 97].append(word)
        except:
            pass

    return response


def splitWords(listWord: list) -> list:
    """splits word set in 3 parts

    Args:
        listWord (list): wordList

    Returns:
        list: splitter word set
    """

    res = [[], [], []]
    for word in listWord:
        if len(word) == 1 or word[1] < "h":
            res[0].append(word)
        elif word[1] >= "i" and word[1] < "r":
            res[1].append(word)
        else:
            res[2].append(word)
    return res


def fileSplit(listWord: list) -> list:
    """splits entire format in db format

    Args:
        listWord (list): output from readTrainingFile

    Returns:
        list: input for db save
    """

    res = [splitWords(wordset) for wordset in listWord]
    return res


def writeWordToFile(filePath: str, word: str):
    """Writes word to file filePath

    Args:
        filePath (str): filePath
        word (str): word to write
    """
    try:
        # print(word)
        fileObj = open(filePath, "r")
        lines = fileObj.read().split("\n")[:-1]
        fileObj.close()

        wordCount = len(lines)
        # print("--")
        if wordCount == 0:
            lines.append(util.getNewWord(word))
        else:
            indx = 0
            while indx < wordCount and util.getWord(lines[indx]) < word:
                indx += 1
            if indx < wordCount and util.getWord(lines[indx]) == word:
                lines[indx] = util.incrementWordCount(lines[indx])
            if indx < wordCount and util.getWord(lines[indx]) > word:
                lines.insert(indx, util.getNewWord(word))
            if indx == wordCount:
                lines.append(util.getNewWord(word))

        fileContent = ""
        for word in lines:
            fileContent += f"{word}\n"
        fileObj = open(filePath, "w")
        fileObj.write(fileContent)
        fileObj.close()

    except ex:
        print(ex)
        pass


def addNewWord():
    BASE_DIR = os.getcwd()
    TRAINING_DATA_PATH = os.path.join(BASE_DIR, "data", "train_data_set")
    RESULT_DATA_PATH = os.path.join(BASE_DIR, "data", "search_data")

    words = str(input("Enter word seprated by space (eg. some,people,are)\n-> ")).split(
        " "
    )
    words = [word for word in words if (len(word) > 0 and word[0] in charSet)]

    for word in words:
        try:
            fileName = os.path.join(RESULT_DATA_PATH, util.getFileName(word))
            writeWordToFile(fileName, word)
            print(f"{word} added to {fileName}")
        except expression as identifier:
            print(f"wrror while adding {word} to {fileName}")
