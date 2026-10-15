import requests

# Reference - https://eonet.gsfc.nasa.gov/docs/v2.1

api_key = "tcPsxbiEDgGpQLZReTn4PgpOVcxcF2taWTg7ywef"

url = "https://eonet.gsfc.nasa.gov/api/v2.1/events"

params = {
    "limit": 5,
    "days": 10
}

response = requests.get(url, params=params, timeout=10)

# Raise an exception if the request failed
response.raise_for_status()

# Convert JSON response into a Python dictionary
data = response.json()

print("Number of events:", len(data["events"]))

for event in data["events"]:
    print("\nEvent:", event["title"])
    print("ID:", event["id"])

    for category in event["categories"]:
        print("Category:", category["title"])

    if event["geometries"]:
        latest = event["geometries"][-1]
        print("Recorded date:", latest["date"])
        print("Coordinates:", latest["coordinates"])
