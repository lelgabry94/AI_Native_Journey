import csv
import os
import json
from datetime import datetime

from typing import List, Dict, Optional

try:
    # Google Sheets API (installed via google-api-python-client dependency)
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except Exception:
    # Keep optional; function will gracefully fall back to CSV if unavailable
    Credentials = None  # type: ignore
    build = None  # type: ignore
    HttpError = Exception  # type: ignore

def _csv_fallback(structured_data: List[Dict], base_filename: str = "auracraft_content_plan") -> None:
    """Write CSV fallback locally."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_filename = f"{base_filename}_{timestamp}.csv"

    if not structured_data:
        print("No data to export.")
        return

    headers = list(structured_data[0].keys())

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(structured_data)

    print(f"✅ Content plan exported to: {csv_filename}")
    print(f"📊 Exported {len(structured_data)} posts successfully!")
    print(f"📋 File contains columns: {', '.join(headers)}")


def _load_service_account_credentials() -> Optional["Credentials"]:
    """Load Google service account credentials from env or file.

    Priority:
    1) GOOGLE_SERVICE_ACCOUNT_JSON (JSON string)
    2) GOOGLE_SERVICE_ACCOUNT_FILE (path)
    3) client_secret.json in current directory
    """
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]

    # JSON content in env
    json_env = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
    if json_env:
        try:
            info = json.loads(json_env)
            return Credentials.from_service_account_info(info, scopes=scopes)  # type: ignore[attr-defined]
        except Exception as e:
            print(f"⚠️  Could not parse GOOGLE_SERVICE_ACCOUNT_JSON: {e}")

    # File path in env
    json_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
    if json_path and os.path.exists(json_path):
        try:
            return Credentials.from_service_account_file(json_path, scopes=scopes)  # type: ignore[attr-defined]
        except Exception as e:
            print(f"⚠️  Could not load GOOGLE_SERVICE_ACCOUNT_FILE: {e}")

    # Default file name
    default_path = "client_secret.json"
    if os.path.exists(default_path):
        try:
            return Credentials.from_service_account_file(default_path, scopes=scopes)  # type: ignore[attr-defined]
        except Exception as e:
            print(f"⚠️  Could not load client_secret.json: {e}")

    return None


def get_service_account_email() -> Optional[str]:
    """Return the service account email from available credentials, if any."""
    # Check JSON in env first
    json_env = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
    if json_env:
        try:
            info = json.loads(json_env)
            return info.get("client_email")
        except Exception:
            pass

    # Then file in env
    json_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
    if json_path and os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                info = json.load(f)
                return info.get("client_email")
        except Exception:
            pass

    # Then default file
    default_path = "client_secret.json"
    if os.path.exists(default_path):
        try:
            with open(default_path, "r", encoding="utf-8") as f:
                info = json.load(f)
                return info.get("client_email")
        except Exception:
            pass

    return None

def export_to_google_sheet(structured_data: List[Dict], spreadsheet_id: Optional[str], sheet_name: str = "Sheet1") -> None:
    """Export structured data to Google Sheets if possible; otherwise CSV.

    - Accepts service account credentials from env or local file.
    - If credentials or spreadsheet_id are missing, falls back to CSV.
    """
    # Guard: no data
    if not structured_data:
        print("No data to export.")
        return

    # If spreadsheet id or API not available, fallback to CSV
    if not spreadsheet_id or Credentials is None or build is None:
        print("📝 Google Sheets export unavailable. Creating local CSV export instead...")
        _csv_fallback(structured_data)
        return

    creds = _load_service_account_credentials()
    if not creds:
        print("📝 Google Sheets authentication not configured. Creating local CSV export instead...")
        _csv_fallback(structured_data)
        return

    # Prepare headers and rows
    headers = list(structured_data[0].keys())
    rows = [[post.get(h, "") for h in headers] for post in structured_data]

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheets = service.spreadsheets()

        # Try to detect existing header (first row)
        try:
            result = sheets.values().get(
                spreadsheetId=spreadsheet_id,
                range=f"{sheet_name}!1:1",
            ).execute()
            first_row = result.get('values', [])
        except HttpError:
            first_row = []

        # Append header if necessary
        if not first_row:
            header_body = {"values": [headers]}
            sheets.values().append(
                spreadsheetId=spreadsheet_id,
                range=sheet_name,
                valueInputOption='RAW',
                insertDataOption='INSERT_ROWS',
                body=header_body,
            ).execute()

        # Append data rows
        body = {"values": rows}
        sheets.values().append(
            spreadsheetId=spreadsheet_id,
            range=sheet_name,
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body=body,
        ).execute()

        print("✅ Exported to Google Sheets successfully!")
        print(f"📋 Sheet: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")

    except Exception as e:
        print(f"⚠️  Google Sheets export failed: {e}")
        print("💡 Creating local CSV export instead...")
        _csv_fallback(structured_data)

