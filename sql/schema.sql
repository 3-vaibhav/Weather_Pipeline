CREATE TABLE IF NOT EXISTS raw_api_payloads (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    payload JSONB NOT NULL,
    ingested_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS weather_observations (
    location VARCHAR(100) NOT NULL,
    observed_at TIMESTAMPTZ NOT NULL,
    temperature_c DOUBLE PRECISION,
    relative_humidity_pct INTEGER,
    wind_speed_kmh DOUBLE PRECISION,
    ingested_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (location, observed_at),
    CHECK (
        relative_humidity_pct IS NULL
        OR relative_humidity_pct BETWEEN 0 AND 100
    )
);

CREATE INDEX IF NOT EXISTS idx_weather_observed_at
ON weather_observations (observed_at);
