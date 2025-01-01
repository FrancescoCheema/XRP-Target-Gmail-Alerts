import os
import json

def load_credentials():
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")
    with open(credentials_path, "r") as file:
        return json.load(file)