import csv
import os
from datetime import datetime

def export_to_google_sheet(structured_data, spreadsheet_id, sheet_name="Sheet1"):
    """Export structured data to Google Sheet (with fallback to CSV)"""
    
    # Check if we have authentication
    if not os.path.exists("client_secret.json"):
        print("📝 Google Sheets authentication not configured.")
        print("💡 Creating local CSV export instead...")
        
        # Create CSV export as fallback
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"auracraft_content_plan_{timestamp}.csv"
        
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
        return
    
    # Original Google Sheets functionality would go here
    print("🔄 Google Sheets authentication configured - would export to actual Google Sheet")
    print(f"📋 Would export to: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")

