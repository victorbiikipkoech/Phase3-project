# cli/commands.py
import click
import requests
from tabulate import tabulate
from weather.db import SessionLocal, init_db
from weather.models import City, WeatherData
from datetime import datetime

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

@click.command(name='get_weather')
@click.option('--city', prompt='Enter city name', help='City for weather data')
def get_weather_command(city):
    """Get current weather for a city."""
    get_weather(city)

@click.command(name='show_weather_history')
@click.option('--city', prompt='Enter city name', help='City for weather history')
def show_weather_history(city):
    """Show recorded weather history for a city."""
    db = SessionLocal()
    city_obj = db.query(City).filter_by(name=city).first()

    if not city_obj:
        click.echo(f"City {city} not found in the database.")
    else:
        weather_history = db.query(WeatherData).filter_by(city_id=city_obj.id).all()

        if not weather_history:
            click.echo(f"No recorded weather history for {city}.")
        else:
            headers = ["Timestamp", "Temperature (°C)"]
            data = [(entry.timestamp, entry.temperature) for entry in weather_history]
            table = tabulate(data, headers=headers, tablefmt="pretty")
            click.echo(table)

# Create a Click Group
@click.group()
def cli():
    pass

# Add commands to the group
cli.add_command(get_weather_command)
cli.add_command(show_weather_history)

if __name__ == '__main__':
    cli()
