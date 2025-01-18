import random
import requests
import json

from Utils import screen_cleaner

access_key = "ba324892608932c0cf7dfcac227365ee"
in_currency = "USD"
out_currency = "ILS"


def get_money_interval(difficulty, amount):

    # API URL
    url = f"https://api.currencylayer.com/convert?access_key={access_key}&from={in_currency}&to={out_currency}&amount=1"

    # Make the API request
    response = requests.get(url)

    # Parse the response as JSON
    data = response.json()

    # Extract the exchange result
    exchange_rate = data["result"]

    # Calculate the value in ILS
    total_value = amount * exchange_rate

    # Calculate the interval
    lower_bound = total_value - (5 - difficulty)
    upper_bound = total_value + (5 - difficulty)

    return lower_bound, upper_bound


def get_guess_from_user(amount):

    while True:

        try:
            guess = float(input(f"Guess the value of {amount} USD in ILS: "))
            return guess

        except ValueError:
            print("Invalid input. Please enter a numeric value.")



def play(difficulty):
    amount = random.randint(1, 100)

    # Get the interval
    interval = get_money_interval(difficulty, amount)

    if interval is None:
        print("Game setup failed due to API issues.")
        return

    user_guess = get_guess_from_user(amount)

    # Check if the guess is within the interval

    if interval[0] <= user_guess <= interval[1]:
        print("Congratulations! Your guess was correct!")
        return True

    else:
        print("Sorry, your guess was incorrect.")
        print(f"The correct interval was: {interval}")
        return False






