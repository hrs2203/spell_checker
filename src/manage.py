import sys, spell

option = {
    "run": spell.takeInput,
    "action2": "action2",
    "action3": "action3",
    "action4": "action4",
    "action5": "action5",
}

if __name__ == "__main__":
    command = sys.argv[1]
    print("===========================")
    if command in option.keys():        
        option[command]()
    else:
        print("Invalid Command\nList of possible option")
        for opt in option.keys():
            print(f"{opt}")
    print("===========================")



