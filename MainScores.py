from flask import *
import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

app = Flask(__name__)


def score_server():

    if os.path.exists(SCORES_FILE_NAME):
        try:
            with open(SCORES_FILE_NAME, 'r') as file:
                score = int(file.read())

            # Return the HTML with the score

            return f"""
            <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1>The score is <div id="score">{score}</div></h1>
                    </body>
                </html>
            """
        # Return the error HTML if there is an issue reading the score
        except (ValueError, FileNotFoundError):

            return f"""
                    <html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1><div id="score" style="color:red">ERROR</div></h1>
                        </body>
                    </html>
                      """

        # Return the error HTML if the score file does not exist
    else:
        return f"""
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1><div id="score" style="color:red">ERROR</div></h1>
                    </body>
                </html>
                """


@app.route('/')

def show_score():
    return score_server()

if __name__ == "__main__":
    app.run(debug=True)


