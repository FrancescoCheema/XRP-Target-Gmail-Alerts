# XRP Target Gmail Alerts

A Python-based project to monitor cryptocurrency rates and send email alerts using the Gmail API when the target price has been reached. This project is ideal for those looking to integrate automated notifications with cryptocurrency monitoring functionality. By default, the script will only send alerts about XRP once it reaches $5 but can be modified according to your needs in the crypto_alerts.py file.
This is the coinlayer API documentation https://coinlayer.com/documentation

## Features
- Fetches real-time cryptocurrency rates from the coinlayer API.
- Sends email alerts for specified rate thresholds.
- Uses Gmail API for email automation.
- Configurable parameters for currency monitoring.

## Prerequisites
- Python 3.9 or higher
- A Google Cloud project with Gmail API enabled
- A `credentials.json` file for Gmail API authentication

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/CryptoWhatsappAlerts.git
cd CryptoWhatsappAlerts
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Credentials
1. Download the `credentials.json` file from your Google Cloud project.
2. Place it in the project directory (or specify its location via an environment variable).
3. Add the environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
   ```

### 5. Adjust Configuration (Optional)
- Modify the script parameters in `crypto_alerts.py` to set your preferred cryptocurrency and rate thresholds.

## Usage

### Monitor Cryptocurrency Rates
Run the main script to start monitoring:
```bash
python crypto_alerts.py
```

### Send Email Alerts
Ensure the Gmail API is authorized and configured, then use:
```bash
python send_email.py
```

## File Structure
```
CryptoWhatsappAlerts/
|── crypto_alerts.py       # Monitors cryptocurrency rates
├── google_service.py      # Handles Gmail API interactions
├── send_email.py          # Sends email alerts
├── utils.py               # Helper functions
├── .gitignore             # Excludes sensitive files from Git
├── README.md              # Project documentation
├── requirements.txt       # Dependencies
├── credentials.json       # Gmail API credentials (excluded from Git)
```

## Notes
- The first time you run the email script, you will be prompted to authenticate via a URL.
- Ensure your Google Cloud project is properly configured for Gmail API access.

