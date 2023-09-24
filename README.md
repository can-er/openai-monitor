# OpenAI Monitor

This script monitors the OpenAI website for a specific text and sends a notification via Telegram if the text is not found.

## Prerequisites

1. **Python**: Ensure you have Python 3.x installed.
2. **Dependencies**: Install `selenium` and `requests` packages using pip:
   ```bash
   pip install selenium requests
   ```
3. **Chrome**: Ensure you have Google Chrome installed.
4. **Chromedriver**: Ensure you have the chromedriver for Chrome downloaded and added to your system's PATH.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/can-er/openai-monitor.git
   cd openai-monitor
   ```

2. **Setup Telegram Bot**:
   - Start a chat with the [BotFather](https://t.me/botfather) on Telegram.
   - Create a new bot.
   - After creating the bot, you will get a `YOUR_TELEGRAM_TOKEN`.
   - Start the bot and send any message to it.
   - (optionnal) Retrieve the chat ID by visiting `https://api.telegram.org/botYOUR_TELEGRAM_TOKEN/getUpdates` in a browser. Look for the "id" inside the "chat" object.

3. **Setup the Environment File**:
   Edit the `.env` file in the root of the project and replace `YOUR_TELEGRAM_TOKEN` with your Telegram bot token.

   ```makefile
   TELEGRAM_TOKEN=YOUR_TELEGRAM_TOKEN
   ```

4. **Load Environment Variables**:
   Before running the script, load the environment variables:
   ```bash
   source .env
   ```

5. **Run the Script**:
   ```bash
   python3 main.py
   ```

## Crontab Setup

To run the script every 5 minutes:

1. Open the crontab editor:
   ```bash
   crontab -e
   ```

2. Add the following line to run the script every 5 minutes and log the output:
   ```bash
   */5 * * * * cd ~/openai-monitor && source .env && python3 main.py >> /var/log/openai_monitor.log 2>> /var/log/openai_monitor_error.log
   ```

3. Save and exit the editor.

## Troubleshooting

1. **Ensure all dependencies are installed**: This includes Python packages and browser drivers.
2. **Check the logs**: If using the crontab setup, check `/var/log/openai_monitor.log` and `/var/log/openai_monitor_error.log` for any error messages or logs.
3. **Ensure environment variables are loaded**: If running the script manually, ensure that you've sourced the `.env` file to load the environment variables.
