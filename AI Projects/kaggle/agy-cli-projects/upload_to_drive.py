import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Scopes required to interact with Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def authenticate_drive():
    """Authenticates the user and returns the Google Drive service object."""
    creds = None
    # token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)

def upload_file(service, local_file_path, drive_filename=None):
    """Uploads a local file to Google Drive.
    
    Args:
        service: Authorized Google Drive API service instance.
        local_file_path: Absolute or relative path to the local file.
        drive_filename: Optional name for the file in Google Drive. If omitted, uses local filename.
    """
    if not os.path.exists(local_file_path):
        print(f"Error: Local file '{local_file_path}' does not exist.")
        return None

    if not drive_filename:
        drive_filename = os.path.basename(local_file_path)

    file_metadata = {'name': drive_filename}
    media = MediaFileUpload(local_file_path, resumable=True)

    try:
        print(f"Uploading '{local_file_path}' as '{drive_filename}' to Google Drive...")
        uploaded_file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        
        file_id = uploaded_file.get('id')
        print(f"Success! File uploaded successfully. File ID: {file_id}")
        return file_id
    except Exception as e:
        print(f"An error occurred during upload: {e}")
        return None

if __name__ == '__main__':
    # Initialize the Drive service connection
    try:
        drive_service = authenticate_drive()
        
        # Example upload: Uncomment and replace with a real local file path
        # upload_file(drive_service, 'path/to/local/file.txt', 'DriveFileName.txt')
    except Exception as err:
        print(f"Authentication failed: {err}")
