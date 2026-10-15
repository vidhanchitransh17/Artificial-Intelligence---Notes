import requests

api_key = "2cbb300daa34207af3464d4deb8ec4bb"

url = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(
    url,
    params={
        "q": "Kolkata,IN",
        "appid": api_key,
        "units": "metric",
    },
    timeout=5,
)

response.raise_for_status()
weather = response.json()

print(weather["main"]["temp"])
print(weather["weather"][0]["description"])