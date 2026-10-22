
services:
  postgres:
    image: postgres:16
    container_name: weather_postgres
    restart: unless-stopped

    environment:
      POSTGRES_DB: weather_db
      POSTGRES_USER: weather_user
      POSTGRES_PASSWORD: local_dev_password

    ports:
      - "5433:5432"

    volumes:
      - weather_data:/var/lib/postgresql/data
      - ./sql/schema.sql:/docker-entrypoint-initdb.d/01-schema.sql:ro

    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U weather_user -d weather_db"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  weather_data:
