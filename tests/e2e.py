from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

APPLICATION_URL = "http://127.0.0.1:5000/"



def test_scores_service(url):
    try:
        service = Service('C:\\Program Files\\chromedriver-win64\\chromedriver.exe')
        options = Options()
        driver = webdriver.Chrome(service=service, options=options)


        driver.get(APPLICATION_URL)

        score_element = driver.find_element(By.ID, 'score')
        score = int(score_element.text)

        if 1 <= score <= 1000:
            result = True

        else:
            result = False

    except Exception as e:
        print(f"Error during test execution: {e}")
        result = False

    finally:
        driver.quit()

    return result





def main_function():
    url = APPLICATION_URL

    if test_scores_service(url):
        sys.exit(0)

    else:
        sys.exit(-1)



if __name__ == "__main__":
    main_function()






















# def test_scores_service(app_url):
#     try:
#         response = requests.get(app_url, timeout=5)
#         response.raise_for_status() # Raise an error for HTTP response codes 4xx/5xx
#
#         if "id=\"score\"" in response.text:
#             import re
#             match = re.search(r'<div id="score">(\d+)</div>', response.text)
#             if match:
#                 score = int(match.group(1))
#                 print(score)
#                 return 1 <= score <= 1000
#         return False  # Return False if the score is not found or invalid
#
#     except Exception as e:
#         print(f"An error occurred while testing the score service: {e}")
#         return False
#
#
# def main_function():
#
#     if test_scores_service(APPLICATION_URL):
#         print("Test passed: The score is valid.")
#         sys.exit(0)
#
#     else:
#         print("Test failed: The score is invalid or could not be retrieved.")
#         sys.exit(-1)
#
#
# if __name__ == "__main__":
#     main_function()
