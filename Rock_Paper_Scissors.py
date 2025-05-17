import random
import time
option=["rock", "paper" , "scissors"]
print("Rock......")
time.sleep(1)
print("Paper...")
time.sleep(1)
print("scissors....")
time.sleep(1)
print("Sho....")
time.sleep(1)
user_choice=input().lower()
time.sleep(1)
Computer_choice=random.choice(option).lower()
if user_choice not in option:
	print("your choice doesnt exist in ")
elif user_choice==Computer_choice:
	print("it is a tie")
elif(user_choice=="rock" and Computer_choice== "Scissors") or (user_choice=="paper" and Computer_choice=="Rock") or (user_choice=="Scissors" and Computer_choice=="paper"):
	print("You won!!!")
else:
	print("Computer Won.. you loser, Womp Womp")
print("COmputer CHoose: ",Computer_choice)

