
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from src.transform import transform_weather


def sample_record():
    return {
        "source": "open-meteo",
        "location": "New Delhi",
        "payload": {
            "current": {
                "time": "2026-10-21T19:30",
                "temperature_2m": 26.0,
                "relative_humidity_2m": 67,
                "wind_speed_10m": 2.4,
            }
        },
    }


def test_transform_valid_weather():
    result = transform_weather(sample_record())

    assert result["location"] == "New Delhi"
    assert result["temperature_c"] == 26.0
    assert result["relative_humidity_pct"] == 67
    assert result["wind_speed_kmh"] == 2.4
    assert result["observed_at"].tzinfo == ZoneInfo("Asia/Kolkata")


def test_transform_rejects_invalid_humidity():
    record = sample_record()
    record["payload"]["current"]["relative_humidity_2m"] = 150

    with pytest.raises(ValueError):
        transform_weather(record)


def test_transform_rejects_missing_weather_data():
    record = sample_record()
    record["payload"]["current"].pop("temperature_2m")

    with pytest.raises(ValueError):
        transform_weather(record)
