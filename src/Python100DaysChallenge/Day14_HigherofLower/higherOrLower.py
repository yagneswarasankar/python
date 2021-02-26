import random
from src.Python100DaysChallenge.Day14_HigherofLower.art import logo,vs
from src.Python100DaysChallenge.Day14_HigherofLower.gameData import data


should_continue = True
numberOfPoints = 0
compareElementData = random.choice(data)
comparableElementData = random.choice(data)
print(f'Compare A: {compareElementData["name"]},{compareElementData["description"]} from {compareElementData["country"]}')
print(vs)
print(f'Against B: {comparableElementData["name"]},{comparableElementData["description"]} from {comparableElementData["country"]}')
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
        print(f"you're right! Current Score : {numberOfPoints}")
        compareElementData = comparableElementData
        print(f'Compare A: {compareElementData["name"]},{compareElementData["description"]} from {compareElementData["country"]}')
        comparableElementData = random.choice(data)
        print(vs)
        print(f'Agaginst B: {comparableElementData["name"]},{comparableElementData["description"]} from {comparableElementData["country"]}')
    else:
        print(f"Sorry, that's wrong. Final score: {numberOfPoints}")
        should_continue = False









