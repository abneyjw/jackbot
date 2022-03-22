import asyncio
import logging
import json

from accuweather import (
    AccuWeather,
    ApiError,
    InvalidApiKeyError,
    InvalidCoordinatesError,
    RequestsExceededError,
)
from aiohttp import ClientError, ClientSession

LATITUDE = 36.2168
LONGITUDE = -81.6746
LOCATION_KEY = "334814"
API_KEY = "QIYstLjGNnGZxShlvHW4GnhC0aVpZ7z1"

logging.basicConfig(level=logging.DEBUG)


async def main():
    async with ClientSession() as websession:
        try:
            accuweather = AccuWeather(
                API_KEY, websession, latitude=LATITUDE, longitude=LONGITUDE
            )
            current_conditions = await accuweather.async_get_current_conditions()
            forecast = await accuweather.async_get_forecast(metric=True)
        except (
            ApiError,
            InvalidApiKeyError,
            InvalidCoordinatesError,
            ClientError,
            RequestsExceededError,
        ) as error:
            print(f"Error: {error}")
        else:
            print(current_conditions['Temperature']['Imperial']['Value'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
