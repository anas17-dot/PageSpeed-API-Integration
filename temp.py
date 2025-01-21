import requests
from datetime import datetime

# Function to fetch data from the API
def fetch_pagespeed_data(url, api_key, strategy="mobile"):
    try:
        # API endpoint
        api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy={strategy}&key={api_key}"
        
        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the JSON response
        data = response.json()
        
        # Extract required metrics
        result = {
            "URL": url,
            "Date of Test": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Cumulative Layout Shift": data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"],
            "Total Blocking Time": data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"],
            "Speed Index": data["lighthouseResult"]["audits"]["speed-index"]["displayValue"],
            "Largest Contentful Paint": data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"],
            "First Contentful Paint": data["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"],
            "Screen Type": strategy
        }
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PageSpeed data: {e}")
        return None

api_key = "AIzaSyA6pRqrbTKpyXpz7Q7cZIjgY2AzoRvPs60"
url = "https://buildberg.co/"
data = fetch_pagespeed_data(url, api_key, strategy="mobile")
print(data)
