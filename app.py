#!/usr/bin/env python3

import folium

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
#from flask_socketio import SocketIO

from sql import xsens_db

app = Flask(__name__)

"""@app.route('/',  methods= ['POST']) # main url, with DB
def save_image():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return 'done'
"""
###socketio = SocketIO(app)

"""@app.route('/apply_photo')
def render_file():
    return render_template('apply_photo.html')

@app.route('/upload_done', methods = ['GET','POST'])
def upload_done():
    if request.method =='POST':
        f=request.files['file']
        f.save(secure_filename(f.filename))
    return 'upload sucess!'
"""
'''
def sessions():
    return render_template('session.html')

def messageReceived(method =['GET','POST']):
    print('message was received!')
    
@socketio.on('my event')
def handle_my_custom_event(json, method=['GET','POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
  '''
# def home():
#     return 'Hello, World!'

@app.route('/') # main url, with ROS
def index():
  return render_template("ros.html")

@app.route('/map')
def map():
    return render_template('map.html')

###@app.route('/upload, methods= ['POST'])
###def upload_file():
###    if request.method =='POST':
###        f = reqest.files['image']
###        f.save('uploads/uploaded_file')
###        return jsonify({'sucess': True})
           

# Run app with database
# @app.route('/') # main url, with DB
# def index():
#     # Get data from database
#     # Dictionary
#     gps_data = xsens_db().GetGPS()
#     imu_data = xsens_db().GetIMU()
    
#     # Create map
#     map = folium.Map(location=[45.5233, -122.6759])
#     start_latitude = gps_data[0]['latitude']
#     start_longitude = gps_data[0]['longitude']
#     #print(start_latitude, start_longitude)
    
#     map = folium.Map(location=[start_latitude, start_longitude], tiles="Stamen Toner", zoom_start=16)

#     start_tooltip = "Start location"
#     last_tooltip = "last location"

#     # Create circle pointer on the map
#     folium.CircleMarker(
#         radius=10,
#         location=[start_latitude, start_longitude],
#         popup=start_tooltip,
#         color="crimson",
#         fill=False
#     ).add_to(map)

#     folium.CircleMarker(
#         radius=10,
#         location=[37.4551, 126.950],
#         popup=last_tooltip,
#         color="blue",
#         fill=False
#     ).add_to(map)

#     # Show and save the map
#     map.add_child(folium.LatLngPopup())
#     map.save('templates/map.html')
    
#     return render_template("showDB.html", gps_data=gps_data, imu_data=imu_data)

host = '0.0.0.0'
port = '9900'

if __name__=='__main__':
    app.run(host=host, port=port, debug=True)
    