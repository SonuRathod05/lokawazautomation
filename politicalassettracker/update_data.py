import json
import datetime

# In the future, you can write code here to fetch data from a CSV, 
# a Google Sheet API, or an external database.
# For now, let's simulate updating the timestamp and data structure.

new_data = {
    "last_updated": str(datetime.date.today()),
    "mps": [
        {
            "id": "pemmasani",
            "house": "ls",
            "name": "Dr. Chandra Sekhar Pemmasani",
            "party": "TDP",
            "totalAssets": 5705,
            "netWorth": 4667
        }
        # Add more MPs here or load them dynamically from your data source
    ]
}

# Automatically overwrite data.json with the latest verified values
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)

print("Successfully updated data.json!")