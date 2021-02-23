import random
from src.Python100DaysChallenge.Day11.art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_option = input("Do you want to play the game blackJack :  Y for YES and N for NO : ")
if play_option == "Y":
    print(logo)
    my_sum = 0
    comp_sum = 0
    my_num  = []
    first_num  = random.choice(cards)
    second_num  = random.choice(cards)
    if first_num + second_num > 21:
        second_num = random.choice(cards)
    comp_first_num = random.choice(cards)
    comp_num = []
    my_num.extend([first_num,second_num])
    # print(f"Your cards: {my_num} , current score : {sum(my_num)}")
    # print(f"Computer's first card: {comp_first_num}")
    should_continue = True


    def compGame(n):
        comp_num = [n]
        while sum(comp_num) <= 17:
            comp_num.append(random.choice(cards))
        print(f"Computer's final hand: {comp_num}, final score: {sum(comp_num)}")
        return sum(comp_num)


    while should_continue :
        print(f"Your cards: {my_num} , current score : {sum(my_num)}")
        print(f"Computer's first card: {comp_first_num}")
        proceed = input(f"Type 'y' to get another card, type 'n' to pass: ")
        if  proceed == "n" :
            print(f"Your final hand: {my_num}, final score: {sum(my_num)}")
            #compResult =compGame(comp_first_num)
            should_continue = False

        else:
            my_num.append(random.choice(cards))
            if sum(my_num) > 21:
                print(f"Your final hand: {my_num}, final score: {sum(my_num)}")
                #compResult =compGame(comp_first_num)
                should_continue = False
    compResult = compGame(comp_first_num)
    if sum(my_num) > 21:
        print(f"My Number : {sum(my_num)}")
        print(f"Comp Number: {compResult}")
        print("You went over. You lose")
    elif sum(my_num) == compResult:
        print(f"My Number : {sum(my_num)}")
        print(f"Comp Number: {compResult}")
        print("Match drawn")
    elif (sum(my_num) < compResult) and compResult <=21:
        print(f"My Number : {sum(my_num)}")
        print(f"Comp Number: {compResult}")
        print("The dealer Wins")
    else:
        print(f"My Number : {sum(my_num)}")
        print(f"Comp Number: {compResult}")
        print("You Won")















