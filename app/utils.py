import requests

from app.models import User

BASE_API_ENDPOIND = 'http://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'
APP_ID = 'b21a2633ddaac750a77524f91fe104e7'


def get_weather_data(city: str) -> dict:
    """ Get weather data by city

    Args:
        city (str):

    Returns:
        dict: response of weather data
    """

    url = BASE_API_ENDPOIND + f'?q={city}&units={UNITS}&appid={APP_ID}'
    response = requests.get(url).json()

    return response


def is_comfortable_temperature(user: User, temp: int) -> bool:
    """_summary_

    Args:
        user (str): user instanse
        temp (int): user comfortable temperature

    Returns:
        bool: temp is comfortable temperature
    """

    if user.is_authenticated:
        return user.comfortable_temperature == temp

    return False
