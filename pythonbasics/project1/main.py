'''
1 snake
-1 water
0 gun
'''
import random
computer=random.randint(-1,1)
you=input("Enter your choice: snake, water, gun: ")
youdict = {
    "snake": 1, 
    "water": -1,
    "gun": 0
}
reversedict = {
     1:"snake", 
     -1:"water",
     0:"gun"
}
print("Computer's choice: ", reversedict[computer])
younum= youdict[you]    

if computer == younum:
    print("It's a tie!")

elif (computer == 1 and younum == -1) or (computer == -1 and younum == 0) or (computer == 0 and younum == 1):
    print("You lose!")  

elif (computer == -1 and younum == 1) or (computer == 0 and younum == -1) or (computer == 1 and younum == 0):   
    print("You win!")   
else:
    print("Invalid input!")