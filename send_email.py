from google_service import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils import load_credentials
from crypto_alerts import send_xrp_alert
import os

credentials = load_credentials()

CLIENT_SECRET_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com/"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

emailMsg = send_xrp_alert()
mimeMessage = MIMEMultipart()
mimeMessage["to"] = "cekkosingh@gmail.com"
mimeMessage["subject"] = "XRP Alert"
mimeMessage.attach(MIMEText(emailMsg, "plain"))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

try:
  message = service.users().messages().send(userId="me", body={"raw": raw_string}).execute()
  print(message)
except Exception as e:
    print("Failed to send email:", e)
