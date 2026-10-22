from datetime import datetime
from zoneinfo import ZoneInfo


def transform_weather(record):
    try:
        current = record["payload"]["current"]
        location = record["location"]
        observed_at = datetime.fromisoformat(current["time"])

        if observed_at.tzinfo is None:
            observed_at = observed_at.replace(
                tzinfo=ZoneInfo("Asia/Kolkata")
            )

        temperature = float(current["temperature_2m"])
        humidity = int(current["relative_humidity_2m"])
        wind_speed = float(current["wind_speed_10m"])

    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"Invalid weather payload: {exc}") from exc

    if not isinstance(location, str) or not location.strip():
        raise ValueError("Location must be a non-empty string")
    if not -100 <= temperature <= 70:
        raise ValueError("Temperature is outside the accepted range")
    if not 0 <= humidity <= 100:
        raise ValueError("Humidity must be between 0 and 100")
    if wind_speed < 0:

        raise ValueError("Wind speed cannot be negative")

    return {
        "source": record.get("source", "open-meteo"),
        "location": location.strip(),
        "observed_at": observed_at,
        "temperature_c": temperature,
        "relative_humidity_pct": humidity,
        "wind_speed_kmh": wind_speed,
    }
