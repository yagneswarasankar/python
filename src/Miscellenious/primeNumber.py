def checkPrime(n):
    is_prime = True
    num = 2
    while num in range(2,round(n/2)+1) and is_prime:
        if n % num == 0:
            is_prime = False
    if is_prime:
        print("The number is prime")
    else:
        print("The number is not a prime")

number = int(input("Enter the number to check: "))
checkPrime(n=number)


