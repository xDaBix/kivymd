import random

youdict = {
    "snake": 1,
    "water": -1,
    "gun": 0
}

reversedict = {
    1: "snake",
    -1: "water",
    0: "gun"
}

computer = random.choice([1, -1, 0])
you = input("Enter your choice (snake, water, gun): ").strip().lower()

if you not in youdict:
    print("Invalid input! Please choose from snake, water, or gun.")
else:
    younum = youdict[you]
    print("Computer's choice:", reversedict[computer])
    
    result = computer - younum
    if result == 0:
        print("It's a tie!")
    elif result == 1 or result == -2:
        print("You win!")
    elif result == -1 or result == 2:
        print("You lose!")
    else:   
        print("Invalid input!")