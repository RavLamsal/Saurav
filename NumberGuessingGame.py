import random
import time
i=list(range(50))
wrongturns=1
Computer_Choice=random.choice(i)
print("So, in this game")
time.sleep(0.4)
print("you have to")
time.sleep(0.4)
print("Choose a number")
time.sleep(0.4)
print("Between 0-49")
time.sleep(0.5)
Response=input('you ready? Click "y" if you are ready, you may click "n" if you wish to exit or you are not ready:  ')
# str.upper(Response)
while True:
    if(Response=="y"):
        UserChoice=int(input("Guess the number from 0-49: "))
        if(UserChoice==Computer_Choice):
            # print("you guessed the number in ",wrongturns, "tries")
            break
        elif(UserChoice>Computer_Choice):
            print("Guess again, you guess quite higher than the choosen number")
            wrongturns+=1
        elif(UserChoice<Computer_Choice):
            print("Guess again, you guessed quite lower than the choosen number")
            wrongturns+=1
if(wrongturns==1):
    print("you guessed number in first try... WOHOHOHOHO, you Rock")
else:
    print("Nah, you suckkkk.. you took like ", wrongturns," tries to guess the number")
print("Number was: ",Computer_Choice)