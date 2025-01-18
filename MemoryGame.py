import time
import random

from Utils import screen_cleaner

lowest_num = 0
highest_num = 101
# list_of_random_numbers = []
# user_list = []


#Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
def generate_sequence(difficulty):
    return [random.randint(lowest_num, highest_num) for _ in range(difficulty)]


#returns a list of numbers prompted from the user. The list length will be in the size of difficulty.
def get_list_from_user(length):
    user_numbers = []

    for _ in range(length):
        while True:
            try:
                answer = int(input("Enter a number: "))
                user_numbers.append(answer)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return user_numbers


#A function to compare two lists if they are equal. The function will return True / False.
def is_list_equal(random_list, user_list):
    return set(random_list) == set(user_list)

#Will call the functions above and play the game. Will return True / False if the user lost or won.
def play(difficulty):

    print("Memorize the following numbers:")
    generated_list = generate_sequence(difficulty)
    print(generated_list)
    time.sleep(0.7) # Display numbers for 0.7 seconds
    # print("\n" * 50)  # Clear the screen (works in most terminals)
    screen_cleaner()

    user_list = get_list_from_user(difficulty)

    if is_list_equal(generated_list, user_list):
        print("Congratulations! You remembered all the numbers correctly!")
        return True
    else:
        print("Sorry, you did not remember the numbers correctly. Better luck next time!")
        return False









