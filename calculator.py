import time
print("this program allows you to perform mathematical operations")
time.sleep(1)
print("you can use operator symbols to do operations")
print("________________________________________")
print('"/" for division')
print('"x" or "*" for Multiplication')
print('"+" for Addition')
print('"-" for Subtraction')
print('"%" for Remainder')
print("________________________________________")
print("Or... If you are trying to calculate simple interest, or any other calculation.. you may select the numbers below")
selection=input('click "SI" for calculating SI(Simple Interest)')
print("________________________________________")
if selection=="SI":
    p=float(input("provide Principal"))
    t=float(input("Provide Time"))
    r=float(input("Provide Rate"))
    print (p*t*r/100)
else:
    X=float(input("Give X for doing Operations: "))
    Y=float(input("Give Y for doing Operations: "))
    print("________________________________________")
    operation=input("provide operator: / , *(x), +, -, %: ")
    iterator=int(input("for how many times do you want to iterate your answer"))
    for i in range(iterator):
        print(f'your operation was "{operation}"')

        if operation=="/":
            Result=X/Y
            print("Division(Result) is : ", Result)
        elif operation== "*" or "x":
            Result=X*Y
            print("Multiplication(Result) is : ", Result)
        elif operation== "+":
            Result=X+Y
            print("Addition(Result) is : ", Result)
        elif  operation== "-":
            Result=X-Y
            print("Subtraction(Result) is : ", Result)
        elif operation=="%":
            Result= X%Y
            print("Remainder(Result) is : ", Result)
        else:
            print("Invalid Operation/Operator selected, that Operator doesnt exist")