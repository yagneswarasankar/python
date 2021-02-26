import random
from src.Python100DaysChallenge.Day14_HigherofLower.art import logo,vs
from src.Python100DaysChallenge.Day14_HigherofLower.gameData import data

def getRandomInt():
    return random.randint(0,len(data) -1)
lengthOfDict = len(data)
random_number = getRandomInt()
should_continue = True
numberOfPoints = 0
compareElement = getRandomInt()
compareElementData = data[compareElement]
#while should_continue:
comparableElement = getRandomInt()
comparableElementData = data[comparableElement]
print(f'{compareElementData["name"]},{compareElementData["description"]} from {compareElementData["country"]}')
print(vs)
print(f'{comparableElementData["name"]},{comparableElementData["description"]} from {comparableElementData["country"]}')
def findMax(first,second):
    if first["follower_count"] > second["follower_count"]:
        return "A"
    else:
        return "B"
while should_continue:
    guess = input("Who has more followers? Type 'A' or 'B':")
    if guess == findMax(compareElementData,comparableElementData) :
        print("findMax" + findMax(compareElementData,comparableElementData))
        numberOfPoints +=1
        compareElementData = data[comparableElement]
        print(f'{compareElementData["name"]},{compareElementData["description"]} from {compareElementData["country"]}')
        comparableElement = getRandomInt()
        comparableElementData = data[comparableElement]
        print(vs)
        print(f'{comparableElementData["name"]},{comparableElementData["description"]} from {comparableElementData["country"]}')
    else:
        print(f"Sorry, that's wrong. Final score: {numberOfPoints}")
        should_continue = False









