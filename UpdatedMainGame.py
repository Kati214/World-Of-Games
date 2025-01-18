import os.path

from Score import add_score
from Utils import *

def welcome(name):

    return(f"Hello {name} and welcome to the World of Games (WoG). \n" 
          f"Here you can find many cool games to play.")

def load_game():

    # Delete the score file at the start of a new session
    if os.path.exists(SCORES_FILE_NAME):
        os.remove(SCORES_FILE_NAME)

    chosen_game = None
    difficulty = None

    while True:

        #Validate Game Choice
        while True:
           screen_cleaner()
           try:
               chosen_game = int(input("Please choose a game to play: \n"
                                       "1. Memory Game - a sequence of numbers will appear for 0.7 seconds and you have to guess it back\n"
                                       "2. Guess Game - guess a number and see if you chose like the computer\n"
                                       "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))

               if chosen_game in [1,2,3]:
                   break # Exit the loop if valid input

               else:
                   print("Invalid choice. Please choose a number between 1 and 3.")

           except ValueError:
               print("Invalid input. Please enter a valid number between 1 and 3.")


        while True:
           #Validate Difficulty Choice
           try:
               difficulty = int(input("Please choose game difficulty from 1 to 5:"))

               if 1 <= difficulty <= 5:
                   break
               else:
                   print("Invalid difficulty level. Please choose a number between 1 and 5.")

           except ValueError:
               print("Invalid input. Please enter a valid number between 1 and 5.")

        #Handle valid inputs and execute the selected game
        result = None

        match chosen_game:
           case 1:
             from MemoryGame import play as memory_play
             result = memory_play(difficulty)

           case 2:
             from GuessGame import play as guess_play
             result = guess_play(difficulty)

           case 3:
             from CurrencyRouletteGame import play as roulette_play
             result = roulette_play(difficulty)

        # Check the result and add score if it is a win
        if result: # True indicates a win
            add_score(difficulty)

        else:
            print("Better luck next time! Your score remains unchanged.")


        # Ask the user if they want to play another game
        play_again = input("Do you want to play another game? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("Thank you for playing! Goodbye!")
            break

welcome("katya")
load_game()


