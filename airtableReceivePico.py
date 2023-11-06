# MUST BE CONNECTED TO WIFI TO USE THIS LIBRARY
# code mainly drawn from airtable website resources

import urequests as requests
import json
from secretStuff import airtable_id, airtable_url, token

# where "Color" is the table name
url = f"{airtable_url}/Color"

# establishes headers to access table
headers = {
    "Authorization": "Bearer " + str(token),
    "Content-Type": "application/json",
}

def receive_color():
    response = requests.get(url, headers=headers) # gets response in json format
    records = response.json()["records"]
    color = str(records[len(records) - 1]["fields"]["COLOR"]) # goes to last entry in COLOR column
    print(color) # prints entry
    return color
