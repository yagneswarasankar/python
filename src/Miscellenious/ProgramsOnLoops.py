# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for num in numbers:
    sum += num

print(sum)

# Range Function:
#It is lazyly evalucations i.e, when it is created it will just store the first number,
#last number and the step and generate the next number on the go.
print(range(10))
print(list(range(10)))
print(list(range(2,8)))
print(range(2,20,3))
print(list(range(2,20,3)))
print(len(range(2,8)))

#Display squares of all number in a list
l = [1,2,3,4,5,6,]
for num in l:
    print(num * num,end = " ")
else:
    print("\n")
    print("The numbers ended")

print(list(range(10,1,-1)))

