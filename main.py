import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

# Constants
URL = "https://openai.com/dall-e-3"
SEARCH_TEXT = "(DALL·E 3 coming soon!)"
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

def send_telegram_notification(message):
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(TELEGRAM_API_URL, data=payload)
    return response.json()

def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    with webdriver.Chrome(options=options) as driver:
        driver.get(URL)
        time.sleep(3)  # Wait for 3 seconds to ensure the page is fully loaded

        # Check if the desired text is present
        if SEARCH_TEXT not in driver.page_source:
            send_telegram_notification(f"The text '{SEARCH_TEXT}' was not found on {URL}!")

if __name__ == "__main__":
    main()
