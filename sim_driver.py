import orhelper
from orhelper import FlightDataType, FlightEvent
import os
import json
import sys
import config

from datetime import datetime

import requests
import json

def openweather_get(lat, lon):
    CACHE = False
    API_KEY = config.API_KEY

    url = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,daily&appid={API_KEY}&units=metric".format(lat=lat,lon=lon, API_KEY=API_KEY)
    #print(url)
    #url2 = "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric".format(lat=lat,lon=lon, API_KEY=API_KEY)
    json_data = {}
    if CACHE:
        raw_data = open("weather_data.json", "r").read()
        json_data = json.loads(raw_data)
    else:
        r = requests.get(url)
        print(r.status_code)
        json_data = json.loads(r.text)
        open("weather_data.json", "w").write(r.text)
    return json_data

def or_run_sim(weather, lat, lon):
    with orhelper.OpenRocketInstance(jar_path="OpenRocket-22.02.jar") as instance:
        # Load document, run simulation and get data and events
        orh = orhelper.Helper(instance)
        doc = orh.load_doc("rocket.ork")
        sim = doc.getSimulation(0)

        opts = sim.getOptions()
        rocket = sim.getRocket()

        driver_data = []
        for i, window in enumerate(weather['hourly']):
             
            """temp = float(window['main']['temp'])
            pressure = float(window['main']['pressure'])
            wind_speed = float(window['wind']['speed'])
            wind_deg = float(window['wind']['deg'])
            lat = float(lat)
            lon = float(lon) """

            temp = float(window['temp'])
            pressure = float(window['temp'])
            wind_deg = float(window['wind_deg'])
            wind_speed = float(window['wind_speed'])

            humidity = float(window['humidity'])
            clouds = float(window['clouds'])
            pop = float(window['pop'])
            try:
                visibility = float(window['visibility'])
            except:
                visibility = None

            lat = float(lat)
            lon = float(lon)
            
            opts.setLaunchLatitude(lat)
            opts.setLaunchLongitude(lon)
            opts.setLaunchPressure(pressure)
            opts.setLaunchTemperature(temp)
            opts.setWindDirection(wind_deg)
            opts.setWindSpeedAverage(wind_speed)

            orh.run_simulation(sim)
            data = sim.getSimulatedData()
            ts = orh.get_timeseries(sim, [FlightDataType.TYPE_TIME, FlightDataType.TYPE_ALTITUDE, FlightDataType.TYPE_VELOCITY_Z])
            sim_data = {
                'flightTime' : data.getFlightTime(),
                'groundHitVelocity' : data.getGroundHitVelocity(),
                'maxAcceleration' : data.getMaxAcceleration(),
                'maxAltitude' : data.getMaxAltitude(),
                'maxVelocity' : data.getMaxVelocity(),
                'timeToApogee' : data.getTimeToApogee() 
            }
            weather_data = {
                'temp' : temp,
                'pressure' : pressure,
                'humidity' : humidity,
                'clouds' : clouds,''
                'precipitation' : pop,
                'visibility' : visibility,
                'wind_speed' : wind_speed,
                'wind_deg' : wind_deg
            }
            window_data = {'dt' : window['dt'],
                           'string_dt' : datetime.utcfromtimestamp(window['dt']).strftime('%Y-%m-%d %H:%M:%S'),
                           'weather_data' : weather_data,
                           'sim_data' : sim_data
                           }
            driver_data.append({'window_data': window_data})
        #print((sim.getRocket().getPosition()))
        #print(window)
    dump = json.dumps(driver_data)
    open("driver_data.json", "w+").write(dump)
    return driver_data

if __name__ == "__main__":
    lat = sys.argv[1]
    lon = sys.argv[2]
    weather = openweather_get(lat, lon)
    driver_data = or_run_sim(weather, lat, lon)