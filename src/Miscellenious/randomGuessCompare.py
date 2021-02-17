from random import randint
choice = True
while choice:
    inp = int(input("Enter the number : "))
    rand = randint(1,9)
    if inp == rand:
        print(f"Randome number is : {rand}")
        print("Good guess. You won")
        choice = False
    else:
        print(f"Random Number is : {rand}")
        print("Try again !")
