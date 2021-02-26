import random
logo = ''' 
    / ____|                        | |  | |                                    | |                
   | |  __  _   _   ___  ___  ___  | |_ | |__    ___   _ __   _   _  _ __ ___  | |__    ___  _ __ 
   | | |_ || | | | / _ \/ __|/ __| | __|| '_ \  / _ \ | '_ \ | | | || '_ ` _ \ | '_ \  / _ \| '__|
   | |__| || |_| ||  __/\__ \\__ \ | |_ | | | ||  __/ | | | || |_| || | | | | || |_) ||  __/| |   
    \_____| \__,_| \___||___/|___/  \__||_| |_| \___| |_| |_| \__,_||_| |_| |_||_.__/  \___||_|   
'''
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
diff_level = input("Choose a difficulty. Type 'easy' or 'hard':")
num = random.choice(range(1,101))
print(f"The number is :{num}")

def returnGuess(str):
    if str == "hard":
        return 5
    elif str == "easy":
        return 10
    else:
        print("Wrong Input")
num_attempts = returnGuess(diff_level)
print(f"you have {num_attempts} attempts to guess the number")

def guessNumber(num,num_attempts):
    num_attempts -=1
    while  num_attempts > 0 :
        guess = int(input("guess the number: "))
        if num < guess :
            print(f"Too high \nGuess again\nYou have {num_attempts} attempts remaining to guess the number.")
        elif num > guess :
            print(f"Too low \nGuess again\nYou have {num_attempts} attempts remaining to guess the number.")
        elif num == guess:
            print("You got it.")
            num_attempts = 0
        else:
            print(f"You got it! The answer was {num}")

guessNumber(num,num_attempts)

