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










