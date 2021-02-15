from turtle import clear

from hangman_art import stages,logo
from hangman_word import word_list
from random import choice
from os import system

def clear():
    system('cls')
#Constants needed
letters_to_display = []
print(logo)
chosen_word  = choice(word_list).lower()
length_of_chosen_word = len(chosen_word)
lives = 6
print(chosen_word)

for _ in chosen_word:
    letters_to_display += "_"
print(letters_to_display)

end_game = False

while not end_game: #"_" in letters_to_display:
    guess = raw_input("Guess a letter: ").lower()
    clear()
    print("guessed letter is : " + guess)
    if guess in letters_to_display:
        print("The letter already guessed")
    cnt = 0
    for num in range(length_of_chosen_word):
        if guess == chosen_word[num]:
          letters_to_display[num] = guess
          cnt = 1
    print(letters_to_display)
    if cnt == 0:
        lives -= 1
        if lives == 0:
            end_game = True
            print("you lose")
    if "_" not in letters_to_display:
        end_game = True
        print("you win")
    print(stages[lives])











