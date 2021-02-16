choice = True
while choice:
    unit = input("Enter the temperature D for degrees and F for foreignheit: ").lower()
    value = float(input("Enter the temperature :"))
    if unit == "f":
        result = 5 * (( value - 32)/9)
        print(f"The result in Degrees is : {result}")
    elif unit == "d":
        result = 9 * (value / 5) + 32
        print(f"The result in Foregnheit: {result}")
    choice = input("Do you want  to continue : y for yes and n for no: ")
    if choice == "y":
        choice = True
    else:
        print("good bye")
        choice = False