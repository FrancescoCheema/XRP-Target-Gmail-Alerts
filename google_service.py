import pickle
import os
import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

"""Communication with Gmail API"""

SCOPES = ['https://mail.google.com/']
TOKEN_FILE = 'token.json'
CREDENTIALS_FILE = 'credentials.json'

def Create_Service(api_name, api_version, client_secret_file=None):
    creds = None

    # Use token.json if it exists and is valid
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        if creds and creds.valid:
            print(f"{api_name} service created successfully using token.json")
            return build(api_name, api_version, credentials=creds)

        print(f"{api_name} service created successfully using {client_secret_file}")
        return build(api_name, api_version, credentials=creds)
    
    raise RuntimeError("No valid credentials found. Please provide a valid token.json or credentials.json file.")

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt

