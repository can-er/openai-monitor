# OpenAI Monitor Script

This script monitors the OpenAI website for the presence of the text "(DALL·E 3 coming soon!)".

## Installation

### Dependencies

1. **Python**: Ensure you have Python 3 installed.
2. **Selenium & BeautifulSoup**: Install the required Python libraries:
   ```bash
   pip install selenium beautifulsoup4
   ```

> :warning: **Geckodriver**: Ensure you have the geckodriver for Firefox downloaded and added to your system's PATH.

### Script Setup

1. **Directory Creation**:
   ```bash
   sudo mkdir -p /opt/openai_monitor
   ```

2. **Place the Script**:
   Copy the `openai_monitor.py` script to `/opt/openai_monitor/`.

3. **Set Permissions**:
   Make the script executable:
   ```bash
   sudo chmod +x /opt/openai_monitor/openai_monitor.py
   ```

4. **Crontab Setup**:
   Open the crontab editor:
   ```bash
   crontab -e
   ```

   Add the following line to run the script every 5 minutes:
   ```bash
   */5 * * * * /usr/bin/python3 /opt/openai_monitor/openai_monitor.py >> /var/log/openai_monitor.log 2>> /var/log/openai_monitor_error.log
   ```

   Save and exit the editor.

## Usage

Once set up, the script will run automatically every hour. It will check the OpenAI website for the specified text and log the results:

- Standard output (e.g., found messages) will be logged to `/var/log/openai_monitor.log`.
- Errors will be logged to `/var/log/openai_monitor_error.log`.

## Troubleshooting

1. **Check Logs**: If you suspect the script isn't working as expected, check the log files for any error messages or outputs.
2. **Dependencies**: Ensure all dependencies are correctly installed and accessible to the script.
