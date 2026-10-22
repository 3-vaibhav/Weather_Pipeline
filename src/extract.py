import requests

API_URL = "https://api.open-meteo.com/v1/forecast"
LOCATION = "New Delhi"
LATITUDE = 28.6139
LONGITUDE = 77.2090


def fetch_weather():
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "Asia/Kolkata",
    }

    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    if "current" not in data:
        raise ValueError("Missing current weather data")

    return {
        "source": "open-meteo",
        "location": LOCATION,
        "payload": data,
    }


def main():
    result = fetch_weather()
    current = result["payload"]["current"]

    print("Location:", result["location"])
    print("Observed at:", current["time"])
    print("Temperature:", current["temperature_2m"], "C")
    print("Humidity:", current["relative_humidity_2m"], "%")
    print("Wind speed:", current["wind_speed_10m"], "km/h")


if __name__ == "__main__":
    main()
