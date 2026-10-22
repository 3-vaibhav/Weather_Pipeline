
from src.extract import fetch_weather
from src.transform import transform_weather
from src.load import load_weather


def main():
    print("Starting weather pipeline...")

    raw_record = fetch_weather()
    print("1/3 Extract complete")

    clean_record = transform_weather(raw_record)
    print("2/3 Transform complete")

    load_weather(raw_record, clean_record)
    print("3/3 Load complete")

    print("Weather pipeline finished successfully!")


if __name__ == "__main__":
    main()
