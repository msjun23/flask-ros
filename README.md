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
전체 [html 스크립트](/templates/subscriber.html)에서 해당 내용을 확인 가능하다.

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

# Trouble shooting
- 해당 스크립트의 경우엔 sensor_msgs/CompressedImage만 스트림 가능하다. Subscribe할 토픽 자료형과 토픽명을 모두 바꿔봤지만 sensor_msgs/Image 토픽은 스트림 불가했다.

- 외부 네트워크에서 해당 웹 페이지를 볼 수는 있지만, 토픽 내용이 업데이트 되지는 않는다. html 스크립트 자체에서 ros topic을 subscribe 하기 때문에 ROS 네트워크가 존재하는 local에서 웹에 접속했을 때만 웹 페이지로 토픽이 올라가진다. 외부 네트워크와 교류하기 위해서는 다른 방법이 필요하다.




