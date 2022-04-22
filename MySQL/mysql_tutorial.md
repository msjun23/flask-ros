# 참고자료
> - [MySQL 설치](https://velog.io/@seungsang00/Ubuntu-%EC%9A%B0%EB%B6%84%ED%88%AC%EC%97%90-MySQL-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)
> - [MySQL 수업(조금 엣날거)](https://opentutorials.org/course/195)

---

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

# MySQL workbench 사용법
![mysql_workbench](/MySQL/images/mysql_workbench.png)

