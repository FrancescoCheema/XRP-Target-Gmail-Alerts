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

def Create_Service(client_secret_file, api_name, api_version, scopes):
    try:
        credentials = service_account.Credentials.from_service_account_file(
            client_secret_file, scopes=scopes
        )
        service = build(api_name, api_version, credentials=credentials)
        print(f"{api_name} service created successfully")
        return service
    except Exception as e:
        print("Unable to connect.")
        print(e)
        return None


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt

