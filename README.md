# flask-ros
Streaming ROS topic at flask web.

It's **not** a ROS package!

---

# ROS websocket 실행
```bash
$ roslaunch rosbridge_server rosbridge_websocket.launch
```

해당 launch 파일만 실행하면 ROS 네트워크와 웹소켓 간의 통신이 가능하다. ROS 네트워크에서 돌아다니는 토픽을 flask에서 호출하는 html 스크립트에서 subscribe해 사용 가능

# ROS Topic -> Flask web

> roslibjs의 예시는 [이 스크립트](/templates/tutorial.html)에서 확인 가능하다.

먼저 [app.py](/app.py)를 확인할 필요가 있다.

![url_ros](/images/url_ros.png)

위 부분만 주석 해제하고 다른 app.route()는 모두 주석처리 해야한다.

아래 내용은 [html 파일](/templates/subscriber.html)과 [JavaScript 파일](/static/subscriber.js)에서 확인 가능하다. html에서 페이지의 모양을 만들고, 자바스크립트를 호출하여 기능을 수행한다.

1. 다음과 같이 subscribe한 토픽을 출력할 자리를 먼저 정의한다. 위도와 경도, 고도의 경우엔 텍스트 형식으로, 이미지의 경우엔 당연히 이미지로 만들었다.

![topic_seat](/images/topic_seat.png)

2. ROSLIB 객체를 생성한다.

![roslib](/images/roslib.png)

3. 다음과 같이 subscribe 문을 작성한다.

![sub](/images/sub.png)

# Test
[app.py](app.py) 스크립트가 위치하는 곳에서 해당 파일을 실행시켜준다.
```bash
$ python3 app.py
```

그 다음 [rosbridge_websocket](#ros-websocket-실행)을 실행한다.
```bash
$ roslaunch rosbridge_server rosbridge_websocket.launch
```

이제 웹 페이지와 rosbridge는 준비된 상태이고, 웹에서 확인하고자 하는 센서 데이터를 publish하면 된다.

예제 파일은 [data](/data/)에 rosbag 파일로 올려두었다. 각각의 파일을 별도의 터미널에서 실행시켜주면 된다.
```bash
# -l means loop
$ rosbag play -l ~/bagfiles/xsens_mti.bag
$ rosbag play -l ~/bagfiles/duckpod_sim_cam_compressed.bag
```

다음과 같이 웹에서 센서 토픽을 확인할 수 있다.

![res](/images/res.png)

# Flask with DB
**MySQL**에 관한 간단한 사용법은 이 [링크](/MySQL/mysql_tutorial.md)에서 확인 가능하다.

```bash
$ pip3 install folium
```

위 명령어를 통해 맵을 띄울 수 있는 라이브러리인 folium을 설치한다.

```python
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
```

[app.py](/app.py) 에서 위 부분만 사용한다. 다른 @app.route() 는 모두 주석 처리 해야한다. 데이터베이스에 xsens_mti 센서의 값이 잘 저장되었다면 아래와 같이 결과를 확인할 수 있다.

![db_res1](/images/db_res1.png)
![db_res2](/images/db_res2.png)

# Trouble shooting
- 해당 스크립트의 경우엔 sensor_msgs/CompressedImage만 스트림 가능하다. Subscribe할 토픽 자료형과 토픽명을 모두 바꿔봤지만 sensor_msgs/Image 토픽은 스트림 불가했다.

- ~~외부 네트워크에서 해당 웹 페이지를 볼 수는 있지만, 토픽 내용이 업데이트 되지는 않는다. html 스크립트 자체에서 ros topic을 subscribe 하기 때문에 ROS 네트워크가 존재하는 local에서 웹에 접속했을 때만 웹 페이지로 토픽이 올라가진다. 외부 네트워크와 교류하기 위해서는 다른 방법이 필요하다.~~




