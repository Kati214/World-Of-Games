import os


SCORES_FILE_NAME = "Scores.txt"
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5

# Read the score in the scores file, if it fails it will create a new one and will use it to save the current score
def add_score(difficulty):

    points_of_winning = (difficulty * 3) + 5

    # Check if the scores file exists
    if not os.path.exists(SCORES_FILE_NAME):
        # Create the file and initialize the score
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(points_of_winning))
        print(f"New score file created. Your current score is: {points_of_winning}")

    else:
        # Read the current score from the file
        try:
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read())

        # Handle case where file contents are invalid
        except ValueError:
            print("Invalid data in score file. Resetting score.")
            current_score = 0

        # Update the score
        new_score = current_score + points_of_winning


        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
        print(f"Your new score is: {new_score}")















