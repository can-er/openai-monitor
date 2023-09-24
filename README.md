# OpenAI Monitor Script

This script monitors the OpenAI website for the presence of the text "(DALL·E 3 coming soon!)" and sends a notification via Telegram if the text is not found.

## Installation

### Dependencies

1. **Python**: Ensure you have Python 3 installed.
2. **Selenium & BeautifulSoup**: 
   ```bash
   pip install selenium beautifulsoup4
   ```

> :warning: **Geckodriver**: Ensure you have the geckodriver for Firefox (or any other browser driver) downloaded and added to your system's PATH.

### Script Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/can-er/openai-monitor.git ~/openai-monitor
   ```

2. **Setup the Environment File**:
   Edit the `.env` file in the root of the project and replace `YOUR_TOKEN` and `YOUR_CHAT_ID` with your Telegram bot token and chat ID respectively:
   ```makefile
   TELEGRAM_TOKEN=YOUR_TOKEN
   TELEGRAM_CHAT_ID=YOUR_CHAT_ID
   ```

3. **Crontab Setup**:
   Open the crontab editor:
   ```bash
   crontab -e
   ```

   Add the following line to run the script every 5 minutes:
   ```bash
   */5 * * * * . ~/openai-monitor/.env; python3 ~/openai-monitor/openai_monitor.py >> ~/logs/openai_monitor.log 2>> ~/logs/openai_monitor_error.log
   ```

## Usage

Once set up, the script will run automatically every 5 minutes. It will check the OpenAI website for the specified text and send a notification to your Telegram if the text is not found.

## Troubleshooting

1. **Check Logs**: If you suspect the script isn't working as expected, check the `~/logs/openai_monitor.log` and `~/logs/openai_monitor_error.log` files for any error messages or outputs.
2. **Dependencies**: Ensure all dependencies are correctly installed and accessible to the script.

