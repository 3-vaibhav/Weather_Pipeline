
import json
import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5433"),
        dbname=os.getenv("DB_NAME", "weather_db"),
        user=os.getenv("DB_USER", "weather_user"),
        password=os.getenv("DB_PASSWORD"),
    )


def load_weather(raw_record, clean_record):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO raw_api_payloads (source, location, payload)
                VALUES (%s, %s, %s)
                """,
                (
                    raw_record["source"],
                    raw_record["location"],
                    json.dumps(raw_record["payload"]),
                ),
            )

            cur.execute(
                """
                INSERT INTO weather_observations (
                    location,
                    observed_at,
                    temperature_c,
                    relative_humidity_pct,
                    wind_speed_kmh
                )
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (location, observed_at)
                DO UPDATE SET
                    temperature_c = EXCLUDED.temperature_c,
                    relative_humidity_pct = EXCLUDED.relative_humidity_pct,
                    wind_speed_kmh = EXCLUDED.wind_speed_kmh,
                    ingested_at = CURRENT_TIMESTAMP
                """,
                (
                    clean_record["location"],
                    clean_record["observed_at"],
                    clean_record["temperature_c"],
                    clean_record["relative_humidity_pct"],
                    clean_record["wind_speed_kmh"],
                ),
            )

        conn.commit()

    print("Raw payload and cleaned observation saved to PostgreSQL.")


if __name__ == "__main__":
    from src.extract import fetch_weather
    from src.transform import transform_weather

    raw = fetch_weather()
    clean = transform_weather(raw)
    load_weather(raw, clean)
