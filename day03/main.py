print("Welcome to Python game")

first = input("pick an option. Left or Right?").lower()
if first == "right":
    print("You loose")
elif first == "left":
    second = input("Swim or wait?").lower()

    if second == "swim":
        print("You loose")
    elif second == "wait":

        third = input("Dig or cave?").lower()
        if third == "dig":
            print("You win!")
        elif third == "cave":
            print("You are out of the game")