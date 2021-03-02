#Printing fibonacci series

# Question 2: Fibonacci Series
#There are plenty of ways to do this .these are the two ways may be we can look at

def fib1(n):
    fib_numbers = [0,1]
    for i in range(2,n):
        fib_numbers.append(fib_numbers[i-1] +fib_numbers[i -2])
    print(fib_numbers)

#fib1(6)

def fib2(n):
    p_num = 0
    cr_num = 1
    print(0,1,end=" ")
    for i in range(0,n-2):
        res = p_num + cr_num
        p_num = cr_num
        cr_num = res
        print(res,end = " ")

#fib2(14)