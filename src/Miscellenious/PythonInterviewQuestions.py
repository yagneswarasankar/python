# #Credit https://pynative.com/python-basic-exercise-for-beginners/
# ##Question 1: Given a two integer numbers return their product and
# ##if the product is greater than 1000, then return their sum
def multiplication_or_sum(a,b):
    product = a * b
    if product >  1000:
        return a + b
    else:
        return product

#print(multiplication_or_sum(300,4))

# ##Question 2: Given a range of first 10 numbers, Iterate from start number to the
# ##end number and print the sum of the current number and previous number

def sum_current_prev_numbers1(n):
    num_set = range(0,n+1)
    for i in range(1,n):
        print(num_set.index(i) + num_set.index(i-1) )

#sum_current_prev_numbers1(7)

def sum_current_prev_numbers2(n):
    prv_num = 0
    for i in range(1,n):
        print(f"current Number is {i} and prev_number is {prv_num}, Sum is : {i + prv_num}")
        prv_num  = i

#sum_current_prev_numbers2(7)

##Question 3:
## Given a string, display only those characters which are present at an even index number.
## index starts from 0
def print_even_sequenced_characters_in_string(str):
    for c in str:
        if str.index(c) % 2 ==1:
            print(c)

#print_even_sequenced_characters_in_string("Girija")

#Question 4: Given a string and an integer number n, remove characters
#from a string starting from zero up to n and return a new string
import string
def strRemove(str,n):
    return str[-n:]

#print(strRemove("Girija sAnkar",4))

def compare_first_and_last_elements(list):
    print(list[0])
    print(list[-1])
    return list[0] == list[-1]

print(compare_first_and_last_elements([1,2,1]))


