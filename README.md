# Weather Data ETL Pipeline 🌦️

Built a simple ETL pipeline using Python to fetch real weather data from the Open-Meteo API, transform and validate it, and store it in PostgreSQL.

### Tech Stack
- Python
- PostgreSQL
- Docker & Docker Compose
- Pandas-free data processing with Python
- Pytest

### What it does
- Fetches weather data for New Delhi from Open-Meteo.
- Validates and transforms temperature, humidity, and wind speed.
- Stores raw API responses and cleaned observations in PostgreSQL.
- Includes unit tests to check data validation.

### Run Locally
```bash
pip install -r requirements.txt
docker compose up -d
python -m src.main
python -m pytest -v
```

Built as a hands-on project to learn API ingestion, ETL workflows, PostgreSQL, Docker, and data quality testing.

**Data source:** [Open-Meteo](https://open-meteo.com/)

**GitHub:** [3-vaibhav](https://github.com/3-vaibhav)
