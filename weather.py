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
        conditions = ["","Sunny","Mostly Sunny","Partly Sunny","Intermittent Clouds",
                      "Hazy Sunshine","Mostly Cloudy","Cloudy","Overcast","","","Fog",
                      "Showers","Mostly Cloudy w/ Showers","Partly Sunny w/ Showers",
                      "Thunderstorms","Mostly Cloudy w/ T Storms","Partly Sunny w/ T-Storms",
                      "Rain","Flurries","Mostly Cloudy w/ Flurries","Partly Sunny w/ Flurries",
                      "Snow","Mostly Cloudy w/ Snow","Ice","Sleet","Freezing Rain","","",
                      "Rain and Snow","Hot","Cold","Windy","Clear","Mostly Clear",
                      "Partly Cloudy","Intermittent Clouds","Hazy Moonlight",
                      "Mostly Cloudy", "Partly Cloudy w/ Showers","Mostly Cloudy w/ Showers",
                      "Partly Cloudy w/ T-Storms","Mostly Cloudy w/ T-Storms",
                      "Mostly Cloudy w/ Flurries","Partly Cloudy w/ Snow"]
        n = 0
        for c in conditions:
            print(str(n) + " " + c)
            n += 1
        LATITUDE = 36.2168
        LONGITUDE = -81.6746
        LOCATION_KEY = "334814"
        API_KEY = "QIYstLjGNnGZxShlvHW4GnhC0aVpZ7z1"
        
        f = open("/home/pi/jackbot/currents.txt")
        content = f.readlines()
        t = time.localtime()
        currTime = int(time.strftime("%H",t)) * 60 + int(time.strftime("%M",t))
        f.close()
        
        print(currTime, '<currtime pasttime>', content[3])
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
                    f.write(conditions[current_conditions['WeatherIcon']] + "\n")
                    print("Current precipitation: " + str(current_conditions['PrecipitationSummary']['Precipitation']['Imperial']['Value']) + "\n")
                    print("Current Weather icon code: " + str(current_conditions['WeatherIcon']) + "\n")
                    t = time.localtime()
                    f.write(str(int(time.strftime("%H",t)) * 60 + int(time.strftime("%M",t))))
                    f.close()
        time.sleep(0.1)
            

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
