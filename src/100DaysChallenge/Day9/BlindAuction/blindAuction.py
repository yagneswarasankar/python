# from replit import clear
from src.BlindAuction.art import logo
import os
#HINT: You can call clear() to clear the output in the console.
print(logo)

def clear():
    os.system("cls")

name_bid = {}
print("Welcome to tbe blind bid: ")
choice = False
while not choice:
    name  = input("Enter the name : ")
    bid_value  = int(input("Enter the Bid: $"))
    name_bid[name] = bid_value
    continueChoice = input("Do you want to continue? please specify yes or no : ").lower()
    if continueChoice == "no":
        choice = True
    clear()

max_bid_value = 0
for name in name_bid:
    if  name_bid[name] > max_bid_value:
        winner_name = name
        winning_bidValue  = name_bid[name]

print(f"The highest bidder is : {winner_name} and bid is ${winning_bidValue}")






  