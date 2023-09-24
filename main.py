import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# OpenAI Monitoring Configuration
URL = "https://openai.com/dall-e-3"
SEARCH_TEXT = "(DALL·E 3 coming soon!)"

# Telegram Configuration
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
MESSAGE = "The text '(DALL·E 3 coming soon!)' is not found anymore on OpenAI's website."

def send_telegram_notification(message):
    """Send a notification message via Telegram."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

def main():
    options = Options()
    options.add_argument('-headless')  # This runs the browser in the background

    with webdriver.Firefox(options=options) as driver:
        driver.get(URL)
        time.sleep(3)  # Wait for 3 seconds
        page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')
    matching_elements = soup.find_all(string=lambda text: SEARCH_TEXT in text)

    if not matching_elements:
        send_telegram_notification(MESSAGE)
        print(f"Text '{SEARCH_TEXT}' not found! Notification sent.")
    else:
        print(f"Text '{SEARCH_TEXT}' found!")

if __name__ == "__main__":
    main()
