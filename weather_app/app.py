import argparse
import requests
from weather.db import SessionLocal, init_db
from weather.models import City, WeatherData
from datetime import datetime
import click

# OpenWeatherMap API Key (replace with your own key)
API_KEY = "14be63389322778fc3863407eb3e9964"

def get_weather_info(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        timestamp = datetime.utcfromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        return temperature, timestamp
    else:
        return None, None

def get_weather(city):
    """Get weather data for a city."""
    db = SessionLocal()
    city_obj = db.query(City).filter_by(name=city).first()

    if not city_obj:
        click.echo(f"City {city} not found. Adding to the database.")
        init_db()  # Initialize the database if not already done
        db.add(City(name=city))
        db.commit()
        city_obj = db.query(City).filter_by(name=city).first()

    temperature, timestamp = get_weather_info(city)

    if temperature is not None and timestamp is not None:
        click.echo(f"Weather in {city} at {timestamp}: {temperature}°C")
        db.add(WeatherData(temperature=temperature, timestamp=timestamp, city_id=city_obj.id))
        db.commit()
    else:
        click.echo(f"Failed to retrieve weather information for {city}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get weather data for a city.')
    parser.add_argument('--city', required=True, help='City for weather data')
    args = parser.parse_args()
    get_weather(args.city)
