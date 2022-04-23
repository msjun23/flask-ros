#!/usr/bin/env python3

import folium

from flask import Flask, render_template, request

from sql import xsens_db

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/') # main url, with ROS
# def index():
#   return render_template("subscriber.html")

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/') # main url, with DB
def index():
    # Get data from database
    # Dictionary
    gps_data = xsens_db().GetGPS()
    imu_data = xsens_db().GetIMU()
    
    # Create map
    map = folium.Map(location=[45.5233, -122.6759])
    start_latitude = gps_data[0]['latitude']
    start_longitude = gps_data[0]['longitude']
    print(start_latitude, start_longitude)
    
    map = folium.Map(location=[start_latitude, start_longitude], tiles="Stamen Toner", zoom_start=16)

    start_tooltip = "Start location"
    last_tooltip = "last location"

    folium.CircleMarker(
        radius=10,
        location=[start_latitude, start_longitude],
        popup=start_tooltip,
        color="crimson",
        fill=False
    ).add_to(map)

    folium.CircleMarker(
        radius=10,
        location=[37.4551, 126.950],
        popup=last_tooltip,
        color="blue",
        fill=False
    ).add_to(map)

    map.add_child(folium.LatLngPopup())
    map.save('templates/map.html')
    
    return render_template("showDB.html", gps_data=gps_data, imu_data=imu_data)

host = '0.0.0.0'
port = '9900'

if __name__=='__main__':
    app.run(host=host, port=port, debug=True)
    