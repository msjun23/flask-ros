create database if not exists gps_db;
use gps_db;

set foreign_key_checks = 0;
drop table if exists gps_data cascade;
drop table if exists imu_data cascade;
set foreign_key_checks = 1;

create table gps_data
(
	seq int not null auto_increment primary key,
    time_stamp timestamp default current_timestamp on update current_timestamp,
	latitude float not null,
	longitude float not null,
	altitude float not null
);
create table imu_data
(
	seq int not null auto_increment primary key,
	time_stamp timestamp default current_timestamp on update current_timestamp,
    quaternion_w float not null,
    quaternion_x float not null,
    quaternion_y float not null,
    quaternion_z float not null,
    linear_acceleration_x float not null,
    linear_acceleration_y float not null,
    linear_acceleration_z float not null,
    angular_velocity_x float not null,
    angular_velocity_y float not null,
    angular_velocity_Z float not null
);
-- insert into imu_data(quaternion_w, quaternion_x, quaternion_y, quaternion_z, linear_acceleration_x, linear_acceleration_y, linear_acceleration_z, angular_velocity_x, angular_velocity_y, angular_velocity_z) values(1.3333333, 1.2222, 1.33333, 1.44444, 1.2223, 23.444, 3.444444, 0.00001, 0.029304, 0.1023904);
-- SELECT seq, time_stamp, quaternion_w, quaternion_x, quaternion_y, quaternion_z, linear_acceleration_x, linear_acceleration_y, linear_acceleration_z, angular_velocity_x, angular_velocity_y, angular_velocity_z FROM imu_data ORDER BY seq DESC LIMIT 1;
-- 
select * from imu_data;
-- 
-- insert into gps_data(latitude, longitude, altitude) values(1.2223, 23.444, 3.444444);
-- 
-- select * from gps_data;
-- SELECT seq, time_stamp, latitude, longitude, altitude FROM gps_data ORDER BY seq DESC LIMIT 1;
-- 
