import os

charSet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

def getWord(string):
    return string.split("=")[0]

def getCount(string):
    try:
        return int(string.split("=")[1])
    except:
        return 0

def getNewWord(word):
    # print(f"{word}=1")
    return f"{word}=1"

def incrementWordCount(string):
    temp = string.split("=")
    count = int(temp[1])+1
    return f"{temp[0]}={count}"


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

    print("============== training data set ==================")

    tempFileList = os.listdir(TRAINING_DATA_PATH)
    fileList = [os.path.join(TRAINING_DATA_PATH, fileName) for fileName in tempFileList]

    for letter in charSet:
        fileName = os.path.join(RESULT_DATA_PATH, f"{letter}.txt")

        if not os.path.exists(fileName):
            open(fileName, "w").close()
        
        for trainFile in fileList:
            textList = readTrainingFile(trainFile, letter)
            for word in textList:
                writeWordToFile(fileName, word)
        print(f"{letter} done.")

    print("=============== training finished ==================")


def readTrainingFile(filePath: str, startChar: str) -> list:
    """Reads file and return unique word list
    starting with startChar

    Args:
        filePath (str): file to read path
        startChar (str): word starting char

    Returns:
        list: list of unique words starting with word
    """

    stopList = [
        ".",",",":",")","(","}","{","[","]"
    ]

    response = list()

    fileObj = open(filePath, "r")
    fileString = fileObj.read()

    # todo: need some work in pre processing
    # train after it's done
    for char in stopList:
        fileString = fileString.replace(char," ")

    fileWord = fileString.split()
    fileWord = [word.lower() for word in fileWord ]

    response = [word for word in fileWord if word[0] == startChar]

    return list(response)

def writeWordToFile(filePath: str, word: str):
    """Writes word to file filePath

    Args:
        filePath (str): filePath
        word (str): word to write
    """
    try:
        fileObj = open(filePath, "r")
        lines = fileObj.read().split("\n")[:-1]
        fileObj.close()

        wordCount = len(lines)
        
        if (wordCount==0):
            lines.append(getNewWord(word))
        else:
            indx = 0
            while ( indx<wordCount and getWord(lines[indx]) < word ):
                indx+=1
            if (indx < wordCount and getWord(lines[indx]) == word ):
                lines[indx]= incrementWordCount(lines[indx])
            if (indx < wordCount and getWord(lines[indx]) > word ):
                lines.insert(indx, getNewWord(word))
            if (indx == wordCount):
                lines.append(getNewWord(word))

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

    words = str(input("Enter word seprated by space (eg. some,people,are)\n-> ")).split(" ")
    words = [word for word in words if ( len(word)>0 and word[0] in charSet ) ]

    for word in words:
        try:
            fileName = os.path.join(RESULT_DATA_PATH, f"{word[0]}.txt")
            writeWordToFile(fileName, word)
            print(f"{word} added to {fileName}")
        except expression as identifier:
            print(f"wrror while adding {word} to {fileName}")
        
    