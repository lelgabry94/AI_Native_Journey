import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json in your project directory.
# This scope grants read/write access to all your Google Sheets.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
TOKEN_FILE = "token.json"
CLIENT_SECRET_FILE = "client_secret.json" # Your downloaded OAuth JSON file

def get_sheets_service():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing Google Sheets API credentials...")
            creds.refresh(Request())
        else:
            print("Authorizing Google Sheets API access for the first time...")
            # The client_secret.json file should be in the same directory as this script
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        print("Google Sheets API service built successfully.")
        return service
    except HttpError as err:
        print(f"Error building Sheets service: {err}")
        return None

def export_to_google_sheet(structured_data: list[dict], spreadsheet_id: str, sheet_name: str = "Content Plan"):
    """
    Exports structured content plan data to a specified Google Sheet.

    Args:
        structured_data (list[dict]): The list of dictionaries, where each dict
                                      is a social media post.
        spreadsheet_id (str): The ID of the Google Sheet to write to.
        sheet_name (str): The name of the specific sheet/tab within the spreadsheet.
    """
    service = get_sheets_service()
    if not service:
        print("Could not get Google Sheets service. Aborting export.")
        return

    # Prepare data for Google Sheets
    # Create header row first based on all possible keys
    all_keys = set()
    for post in structured_data:
        all_keys.update(post.keys())

    # Define a preferred order for headers to make the sheet readable
    # Add any specific key names from your parser that you want in order
    preferred_order = [
        "Day/Date Suggestion",
        "Platform",
        "Post Type",
        "Core Concept/Topic",
        "Draft Caption",
        "Relevant Hashtags",
        "Ai Trend Insight", # Adjust if your parser normalized this differently
        "Image Generation Prompt"
    ]
    # Add any remaining keys not in preferred order (alphabetically)
    headers = [key for key in preferred_order if key in all_keys]
    remaining_keys = sorted([key for key in all_keys if key not in preferred_order])
    headers.extend(remaining_keys)

    values = [headers] # Start with the header row

    # Populate rows with data
    for post in structured_data:
        row = []
        for header in headers:
            row.append(post.get(header, "")) # Use .get() to safely handle missing keys
        values.append(row)

    # Range to append to. We'll append to the first available row in the specified sheet.
    # 'Sheet1!A1' means it will find the last row in Sheet1 starting from A1 and append after that.
    range_name = f"{sheet_name}!A1"

    body = {
        'values': values
    }
    
    try:
        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED", # This preserves formatting (e.g., numbers as numbers)
            insertDataOption="INSERT_ROWS", # Inserts new rows for the data
            body=body
        ).execute()
        print(f"{result.get('updates').get('updatedCells')} cells updated in Google Sheet.")
        print(f"Data successfully exported to Google Sheet: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")
    except HttpError as err:
        print(f"Error exporting data to Google Sheet: {err}")
        print("Please ensure the spreadsheet ID is correct and the service account/user has edit permissions.") 