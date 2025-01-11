import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request 
from google.oauth2.credentials import Credentials

"""Communication with gmail API"""

def Create_Service(client_secret_file, api_name, api_version, *scopes):
    credentials = service_account.Credentials.from_service_account_file(
        client_secret_file, scopes=scopes[0]
    )
    return build(api_name, api_version, credentials=credentials)

    cred = None
    token_file = 'token.json'

    if os.path.exists(token_file):
        cred = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            raise RuntimeError("Headless environment cannot support interactive 0Auth flow. Provide a valid token.json")

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt
