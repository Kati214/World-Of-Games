from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

APPLICATION_URL = "http://127.0.0.1:5000/"


def test_scores_service(url):
    driver = None #Initialize the driver to None
    try:
        service = Service('/usr/bin/chromedriver')
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")  # Required for Docker
        options.add_argument("--disable-dev-shm-usage")  # Prevent resource issues
        driver = webdriver.Chrome(service=service, options=options)


        driver.get(APPLICATION_URL)

        score_element = driver.find_element(By.ID, 'score')
        score = int(score_element.text)


        return 1 <= score <= 1000

    except Exception as e:
        print(f"Error during test execution: {e}")
        result = False

    finally:
        if driver:
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


