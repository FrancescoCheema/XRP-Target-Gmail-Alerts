import requests
import os
import json
from google_service import Create_Service
from utils import load_credentials
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

credentials = load_credentials()

CLIENT_SECRET_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com/"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

"""Added API, exported key to venv environment"""
access_key = os.getenv("ACCESS_KEY")
url = f"http://api.coinlayer.com/live?access_key={access_key}"
params = {
    "symbols" : "XRP",
    "target" : "USD"
}

"""Added thresholds, for when XRP is low, Exceedex, or reaches target"""
threshold = {
    "low" : 2.00,
    "exceeded": 3.00,
    "target": 5.00
}

def send_email(service, subject, emailMsg):

    mimeMessage = MIMEMultipart()
    mimeMessage["to"] = "cekkosingh@gmail.com"
    mimeMessage["subject"] = subject
    mimeMessage.attach(MIMEText(emailMsg, "plain"))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    try:
        message = service.users().messages().send(userId="me", body={"raw": raw_string}).execute()
        print(message)
    except Exception as e:
        print("Failed to send email:", e)

"""get API response in real-time, specifically for XRP and print alerts based off thresholds, XRP price"""
def send_xrp_alert(service):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        xrp_rate = rates.get("XRP")
        if not rates or "XRP" not in rates:
            raise Exception("XRP data is missing or invalid in the API response.")

        if xrp_rate is not None:
            if xrp_rate < threshold["low"]:
                return f"XRP rate is currently at {xrp_rate}. It is now below the threshold."
            elif xrp_rate < threshold["exceeded"]:
                return f"XRP has exceeded the threshold. Currently at {xrp_rate}."
            elif xrp_rate < threshold["target"]:
                subject = "XRP Target Reached"
                emailMsg = f"XRP target reached. The current price is {xrp_rate}"
                send_email(service ,subject, emailMsg)
                return f"XRP has reached the target threshold. Currently at {xrp_rate}."
            else:
                return f"XRP is stable, current rate: {xrp_rate}."
        else:
            raise Exception(f"failed to fetch, status error: {response.status_code}")



try:
    service = load_credentials()
    send_xrp_alert(service)
    print(service)
except Exception as e:
    print("Error:", e)