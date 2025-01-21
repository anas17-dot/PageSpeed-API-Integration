import gspread
from oauth2client.service_account import ServiceAccountCredentials

def add_to_google_sheets(sheet_name, data):
    """
    Add a row of data to a Google Sheet.

    Parameters:
    sheet_name (str): The name of the Google Sheet.
    data (dict): The data to add (key-value pairs).

    """
    try:
        # Define the scope for accessing Google Sheets
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        
        # Authenticate using the credentials file
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)
        
        # Open the Google Sheet by its name
        sheet = client.open(sheet_name).sheet1
        
        # Append the data as a new row
        sheet.append_row(list(data.values()))
        print("Data added to Google Sheet successfully!")
    except Exception as e:
        print(f"Error adding data to Google Sheet: {e}")

# Example data to add to the Google Sheet
data = {
    "URL": "https://buildberg.co/",
    "Date of Test": "2025-01-21 14:30:00",
    "Cumulative Layout Shift": "0.05",
    "Total Blocking Time": "100 ms",
    "Speed Index": "3.4 s",
    "Largest Contentful Paint": "2.8 s",
    "First Contentful Paint": "1.4 s",
    "Screen Type": "mobile"
}

# Call the function
add_to_google_sheets("PageSpeed Data", data)
