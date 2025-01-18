from pickle import APPEND

import requests
import sys

APPLICATION_URL = "http://127.0.0.1:5000/"

def test_scores_service(app_url):
    try:
        response = requests.get(app_url, timeout=5)
        response.raise_for_status() # Raise an error for HTTP response codes 4xx/5xx

        if "id=\"score\"" in response.text:
            import re
            match = re.search(r'<div id="score">(\d+)</div>', response.text)
            if match:
                score = int(match.group(1))
                print(score)
                return 1 <= score <= 1000
        return False  # Return False if the score is not found or invalid

    except Exception as e:
        print(f"An error occurred while testing the score service: {e}")
        return False


def main_function():

    if test_scores_service(APPLICATION_URL):
        print("Test passed: The score is valid.")
        sys.exit(0)

    else:
        print("Test failed: The score is invalid or could not be retrieved.")
        sys.exit(-1)


if __name__ == "__main__":
    main_function()
