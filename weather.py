import asyncio
import logging
import json
import time
from accuweather import (
    AccuWeather,
    ApiError,
    InvalidApiKeyError,
    InvalidCoordinatesError,
    RequestsExceededError,
)
from aiohttp import ClientError, ClientSession

#This script pulls the latest temperature and conditions from AccuWeather given that more than 30 minutes has passed since the last call.
#This is because the free version of the AccuWeather API only allows 50 calls a day.

class Weather:
    async def main():
        LATITUDE = 36.2168
        LONGITUDE = -81.6746
        LOCATION_KEY = "334814"
        API_KEY = "QIYstLjGNnGZxShlvHW4GnhC0aVpZ7z1"
        
        f = open("currents.txt")
        content = f.readlines()
        t = time.localtime()
        currTime = int(time.strftime("%H",t)) * 60 + int(time.strftime("%M",t))
        print(int(content[3]) + 30 < currTime)
        f.close()
        
        if(int(content[3]) + 30 < currTime):
            async with ClientSession() as websession:
                try:
                    accuweather = AccuWeather(
                        API_KEY, websession, latitude=LATITUDE, longitude=LONGITUDE
                    )
                    current_conditions = await accuweather.async_get_current_conditions()
                except (
                    ApiError,
                    InvalidApiKeyError,
                    InvalidCoordinatesError,
                    ClientError,
                    RequestsExceededError,
                ) as error:
                    print(f"Error: {error}")
                else:
                    f = open("currents.txt", "w")
                    f.write(str(current_conditions['Temperature']['Imperial']['Value']) + "\n")
                    f.write(str(current_conditions['PrecipitationSummary']['Precipitation']['Imperial']['Value']) + "\n")
                    f.write(str(current_conditions['WeatherIcon']) + "\n")
                    t = time.localtime()
                    f.write(str(int(time.strftime("%H",t)) * 60 + int(time.strftime("%M",t))))
                    f.close()
        time.sleep(0.1)
            

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
