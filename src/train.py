import os

def train_data():
    BASE_DIR = os.getcwd()
    TRAINING_DATA_PATH = os.path.join(BASE_DIR, "data", "train_data_set")
    RESULT_DATA_PATH = os.path.join(BASE_DIR, "data", "search_data")
    
    print("************Deleting existing data set************")

    

    print("****************** Deleted ***********************")


    print("Done")