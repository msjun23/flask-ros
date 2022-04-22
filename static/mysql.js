var mysql = require('mysql');
console.log('required mysql');

var connection = mysql.createConnection({
    host: 'localhost', // host address
    user: 'aril', // mysql user
    password: '1234', // mysql password
    database: 'gps_db' // mysql database
});

connection.connect();
console.log('Database Connected');

// Connecting to ROS
// -----------------
var roslib = require('roslib');
var ros = new roslib.Ros({
    url: 'ws://localhost:9090'
});

ros.on('connection', function() {
    console.log('Connected to websocket server.');
});

ros.on('error', function(error) {
    console.log('Error connecting to websocket server: ', error);
});

ros.on('close', function() {
    console.log('Connection to websocket server closed.');
});


// Subscribing to a Topic
// ----------------------

// GPS data
var gnss_listener = new roslib.Topic({
    ros: ros,
    name: '/gnss',
    messageType: 'sensor_msgs/NavSatFix'
});

gnss_listener.subscribe(function(message) {
    //    console.log(message.header.stamp)
    //    console.log('latitude :' + message.latitude + ', longitude :' + message.longitude + ', altitude :' + message.altitude);
    connection.query('insert into gps_data(latitude, longitude, altitude) values(' + message.latitude + ', ' + message.longitude + ', ' + message.altitude + ')'),
        function(error, results, fields) {
            if (error) {
                console.log(error);
            }

            console.log(results);
        }
});

// IMU data
var imu_listener = new roslib.Topic({
    ros: ros,
    name: '/imu/data',
    messageType: 'sensor_msgs/Imu'
});

imu_listener.subscribe(function(message) {
    //    console.log("quaternion :" + message.orientation.w, message.orientation.x, message.orientation.y, message.orientation.z)
    //    console.log("linear_acceleration :" + message.linear_acceleration.x, message.linear_acceleration.y, message.linear_acceleration.z)
    //    console.log("angular_velocity : " + message.angular_velocity.x, message.angular_velocity.y, message.angular_velocity.z)
    connection.query('insert into imu_data(quaternion_w, quaternion_x, quaternion_y, quaternion_z, linear_acceleration_x, linear_acceleration_y, linear_acceleration_z, angular_velocity_x, angular_velocity_y, angular_velocity_z) values(' + message.orientation.w + ', ' + message.orientation.x + ', ' + message.orientation.y + ', ' + message.orientation.z + ', ' + message.linear_acceleration.x + ', ' + message.linear_acceleration.y + ', ' + message.linear_acceleration.z + ', ' + message.angular_velocity.x + ', ' + message.angular_velocity.y + ', ' + message.angular_velocity.z + ')'),
        function(error, results, fields) {
            if (error) {
                console.log(error);
            }
            console.log(results);
        }
})

//console.log('Database Disconnected');
//connection.end();