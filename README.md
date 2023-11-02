# Altitude Inc Weather Simulation Tool
This tool was built to test our rocket in various real weather conditions to determine optimal launch windows based on upcoming weather forecasts.

## Disclaimer
This tool was built over the course of about 4 days, and so as a result is far from my best programming or software structuring. It is purely a prototpe and was built to get a demo working in a few days.

Please don't take this project as an example of my best work!

## Architecture
```sim_driver.py``` builds the dataset the UI reads from, it takes in a lat and lon as command line args.

It gathers weather data from openweather API, and connect it to an OpenRocket simulation using Jpype, using orhelper as a middleman for efficiency. 

## Building
```python3 -m venv venv```
```source /venv/bin/activate```
```pip install -r requirements.txt```
```python3 run.py```
