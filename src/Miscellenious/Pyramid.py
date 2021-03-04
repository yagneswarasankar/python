def printPyramidProper(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end =" ")
        print()

#printPyramidProper(6)

def printPyramidReverse(n):
    for i in range(n+1,1,-1):
        for j in range(1,i):
            print(j,end=" ")
        print()

#printPyramidReverse(7)

def alphabetProperPyramid(n):
    for i in range(ord('A'),ord('A') + n + 1):
        for j in  range(ord('A'),i+1):
            print(chr(j),end=" ")
        print()
#alphabetProperPyramid(5)

def repeatedAlphabetProperPyramid(n):
    for i in range(ord('A'),ord('A') + n + 1):
        for j in  range(ord('A'),i+1):
            print(chr(i),end=" ")
        print()
#repeatedAlphabetProperPyramid(5)

def norepeatAlphabetProgram(n):
    for i in range(ord('A') ,ord('A')+n):
        for j in range(ord(chr(i))  , (2 * ord(chr(i)) - ord('A'))+1):
           print(chr(j),end = " ")
        print()

#norepeatAlphabetProgram(5)

# def pascalTriangle(rows):
#     coef = 1
#     for i in (0,rows):
#         for space in range(1,rows +1 - i):
#             print("  ",end=" ")
#             for j in range(0,i+1) :
#                 if j == 0 or i == 0:
#                     coef = 1
#                 else:
#                     coef = coef * (i - j + 1) / j
#                 print(coef)
#
#         print("\n")
# pascalTriangle(5)


from turtle  import Turtle, Screen
import random
turtle_objects = []
for _ in range(5):
    new_turtle = Turtle("turtle")
    turtle_objects.append(new_turtle)
for i in range(6):
    for j in range(i):
        random.choice(turtle_objects)
    print("\n")

my_screen = Screen()
my_screen.exitonclick()

