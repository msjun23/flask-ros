# MySQL Installation
```bash
$ sudo apt udpate
$ sudo apt install mysql-server
```

# MySQL 실행하기
```bash
$ sudo systemctl start mysql
$ sudo systemctl enable mysql
$ sudo mysql -u root -p
```
![mysql](/MySQL/images/mysql.png)

# Create database
```bash
mysql> CREATE DATABASE test;
mysql> SHOW DATABASES;

mysql> DROP DATABASE test;      # database 삭제
```
![show_database](/MySQL/images/show_database.png)

information_schema, mysql, performance_schema, sys는 기본적으로 있는 것 같음.

# 사용자 생성/조회/삭제
```bash
# 생성
mysql> create user '{username}'@'%' identified by '{password}';     # 외부 접속 허용
mysql> create user '{username}'@'localhost' identified by '{password}';     # 외부 접속 불가능

# 데이터베이스에 해당 사용자가 사용할 수 있도록 권한 부여
mysql> grant all privileges on {database}.* to '{username}'@'%' identified by '{password}';     # 외부 접속 허용
mysql> grant all privileges on {database}.* to '{username}'@'localhost' identified by '{password}';     # 외부 접속 불가능

# 반드시 실행
mysql> flush privileges;
```

```bash
# 조회
mysql> select user, host from user;
```

```bash
# 삭제
mysql> drop user '{username}'@'%';              # 외부 접속 허용했을 때
mysql> drop user '{username}'@'localhost';      # 외부 접속 허용 안했을 때

# 반드시 실행
mysql> flush privileges;
```

# .sql 파일 실행
[gps_data.sql](/MySQL/gps_data.sql) 파일을 사용해서 gps와 imu데이터를 저장할 데이터베이스를 생성할 수 있다.

```bash
# MySQL 실행
$ sudo mysql -u root -p

# 사용할 데이터베이스 선택, 구조는 아래와 같다
# 데이터베이스
#   └── 테이블1
#   └── 테이블2
#   └     .
#   └     .
mysql> use {database};

# source 명령어와 sql 파일 경로 지정
mysql> source ~/flask-ros/MySQL/gps_data.sql

# 테이블 생성 확인하기
mysql> show tables;

# 각 테이블에 저장된 값 확인하기
mysql> select * from {tablename}
# mysql> select * from gps_data;
# mysql> select * from imu_data;
```

# MySQL 서버 실행
**[mysql.js](/static/mysql.js) 는 html 스크립트에 포함해서 실행하는게 아님.**

[mysql.js](/static/mysql.js) 는 ros topic을 subscribe하므로 rosbridge_server가 먼저 실행되어야 한다.
```bash
$ roslaunch rosbridge_server rosbridge_websocket.launch
```

다른 터미널에서 [mysql.js](/static/mysql.js)이 위치하는 곳으로 이동한 후 js 스크립트를 실행하면 된다.
```bash
$ node mysql.js
```

이제 테스트를 위해서 local에서 [xsens_mti.bag](/data/xsens_mti.bag) 파일을 실행하면 publish된 센서 값들이 mysql 서버에 저장될 것이다.
> gps 값 -> gps_db/gps_data
> 
> imu 값 -> gps_db/imu_data

다시 테이블에 저장된 값을 초기화하려면
```bash
mysql> truncate {tablename};
# mysql> truncate gps_data;
# mysql> truncate imu_data;
```
