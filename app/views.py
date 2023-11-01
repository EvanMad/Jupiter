from flask import render_template, flash, request, session, url_for, redirect
from app import app
import json

lat = 0
lon = 0

@app.route('/hw')
def index():
    user = {'name' : "Evan Madurai"}

    return "hello world!"

@app.route('/')
def home():
    data = open("driver_data.json").read()
    data_dict = json.loads(data)
    return render_template('dashboard.html',
                           data=data_dict
                           )

@app.route('/coords', methods=["POST"])
def coords():
    json_data = json.loads(request.data)
    lat = json_data['lat']
    lon = json_data['lon']
    return "200"

@app.route('/get_weather', methods=["GET"])
def get_weather():
    return 

@app.route('/<dt>', methods=["GET"])
def open_window(dt):
    data = open("driver_data.json").read()
    data_dict = json.loads(data)
    window_data = {}
    for item in data_dict:
        #print(type(item['window_data']['dt']))
        if(str(item['window_data']['dt']) == (dt)):
            window_data = item['window_data']
    return render_template('sim_page.html',
                           data=window_data
                           )