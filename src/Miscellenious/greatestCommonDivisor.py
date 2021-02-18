def gcd(num1,num2):
    if num1 % num2 == 0:
        print(f"{num2} is gcd" )
    elif num2 % num1 == 0:
        print(f"{num1} is gcd")
    elif num1 > num2:
        gcd(num2,num1 % num2)
    else:
        gcd(num1,num2 % num2)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd(num1,num2)