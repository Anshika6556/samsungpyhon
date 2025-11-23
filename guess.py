# Number Guessing Game
from art import logo

from random import randint #randint(1,100)
# 2 level easy , hard
easy_turns=10
hard_turns=5
# computer num=70
# user num=30
# fuction check answer
def check_answer( guess,answer,no_of_turns):
    if guess>answer:
        print("Too high.")
        return no_of_turns-1
    elif guess<answer:
        print("Too low.")
        return no_of_turns-1
    else:
        print(f"You got it! The answer was {answer} YOU WIN!!")


    

# function set difficulty
def set_difficulty():
    # try while also and also string input type easy or EASY should be considered same.
    input_level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if input_level=='easy':
        return easy_turns
    elif input_level=='hard':
        return hard_turns 
    else:
        print("Invalid input. Please type 'easy' or 'hard'.")
        return set_difficulty()  
# game function
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # computer generate random number
    answer=randint(1,100) #70
    no_of_turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {no_of_turns} attempts remaining to guess the number.")
        #guess from user
        guess=int(input("Make a guess: "))
        no_of_turns=check_answer(guess,answer,no_of_turns)
        if no_of_turns==0:
            print("You've run out of guesses, you LOST THE GAME.")
            return # EXIT FROM FUNCTION GAME 
        elif guess!=answer:
            print("Guess again.")
game()

    