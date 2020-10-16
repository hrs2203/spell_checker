import sys, spell, train

option = {
    "run": spell.takeInput,
    "train": train.train_data,
    "addWord": train.addNewWord,
    "action4": "action4",
    "action5": "action5",
}

if __name__ == "__main__":
    command = sys.argv[1]
    print("===========================")
    if command in option.keys():
        try:
            option[command]()
        except:
            print(f"some error while executing command {command}")       
    else:
        print("Invalid Command\nList of possible option")
        for opt in option.keys():
            print(f"{opt}")
    print("===========================")



