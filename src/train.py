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
        fileName = os.path.join( RESULT_DATA_PATH, f"{letter}.txt" )
        if ( not os.path.exists( fileName ) ):
            open(fileName,"w").close()
        

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

    response = list()

    fileObj = open(filePath, "r")
    fileWord = fileObj.read().split()
    fileWord = [word.lower() for word in fileWord]

    response = [word for word in fileWord if word[0] == startChar]

    return list(response)

