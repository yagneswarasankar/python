
## Usual Arithmatic functions:

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

arthmetic_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("Enter the number: "))
    should_continue = True
    while should_continue:
        for operator in arthmetic_dict:
            print(operator)
        opn = input("Enter the operation from above line: ")
        num2 = float(input("Enter the second number: "))
        function = arthmetic_dict[opn]
        result = function(num1,num2)
        print(f"{num1} {opn} {num2} = {result}")
        choice_to_continue =input(f"Do you want continue with result {result} : ")
        if choice_to_continue == "y":
            num1 = result
        else:
            should_continue = False
            calculator()
calculator()




