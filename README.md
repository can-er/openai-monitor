# OpenAI Monitor Script

This script monitors the OpenAI website for the presence of the text "(DALL·E 3 coming soon!)" and sends a notification via Telegram if the text is not found.

## Installation

### Dependencies

1. **Python**: Ensure you have Python 3 installed.
2. **Selenium & BeautifulSoup**: Install the required Python libraries:
   ```bash
   pip install selenium beautifulsoup4
   ```

> ⚠️ **Geckodriver**: Ensure you have the geckodriver for Firefox (or another browser driver) downloaded and added to your system's PATH.

### Script Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/can-er/openai-monitor.git
   ```

2. **Directory Creation**:
   ```bash
   sudo mkdir -p /opt/openai_monitor
   ```

3. **Place the Script**:
   Copy the `openai_monitor.py` script to `/opt/openai_monitor/`:
   ```bash
   sudo cp openai-monitor/openai_monitor.py /opt/openai_monitor/
   ```

4. **Set Permissions**:
   Make the script executable:
   ```bash
   sudo chmod +x /opt/openai_monitor/openai_monitor.py
   ```

### Environment Variables Setup

1. **Create a Secure Directory for `.env`**:
   ```bash
   sudo mkdir -p /etc/openai_monitor
   ```

2. **Place the `.env` File**:
   Move your `.env` file with the Telegram `TOKEN` and `CHAT_ID` to the secure directory:
   ```bash
   sudo mv /path/to/your/original/.env /etc/openai_monitor/
   ```

3. **Restrict `.env` File Permissions**:
   Ensure that only the root user (or the user running the script) can read the `.env` file:
   ```bash
   sudo chown root:root /etc/openai_monitor/.env
   sudo chmod 600 /etc/openai_monitor/.env
   ```

4. **Crontab Setup**:
   Open the crontab editor:
   ```bash
   crontab -e
   ```

   Add the following line to run the script every hour:
   ```bash
   0 * * * * . /etc/openai_monitor/.env; /usr/bin/python3 /opt/openai_monitor/openai_monitor.py >> /var/log/openai_monitor.log 2>> /var/log/openai_monitor_error.log
   ```

## Usage

Once set up, the script will run automatically every hour. It will check the OpenAI website for the specified text and send a notification to your Telegram if the text is not found.

## Troubleshooting

1. **Check Logs**: If you suspect the script isn't working as expected, check the log files for any error messages or outputs.
2. **Dependencies**: Ensure all dependencies are correctly installed and accessible to the script.

---

This README now includes the step to clone the repository from GitHub as part of the installation process.
