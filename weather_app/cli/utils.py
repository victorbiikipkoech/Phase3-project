import argparse
import click
import pyfiglet
from simple_chalk import chalk
from .commands import get_weather, get_weather_info  # Assuming your commands are in cli/commands.py

def print_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    click.echo(ascii_art)

def display_colored_text(text, color='green'):
    styled_text = getattr(chalk, color)(text)
    click.echo(styled_text)

def parse_command_line_args():
    parser = argparse.ArgumentParser(description='Get weather data for a city.')
    parser.add_argument('--city', required=True, help='City for weather data')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_command_line_args()

    print_ascii_art('Weather App')
    display_colored_text(f"Getting weather data for {args.city}", 'blue')

    get_weather(args.city)
