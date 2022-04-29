// Connecting to ROS
// -----------------

var ros = new ROSLIB.Ros({
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
var gnss_listener = new ROSLIB.Topic({
    ros: ros,
    name: '/gnss',
    messageType: 'sensor_msgs/NavSatFix'
});

gnss_listener.subscribe(function(message) {
    console.log('Received message on ' + gnss_listener.name + ': ' + message.latitude + ', ' + message.longitude + ', ' + message.altitude);
    document.getElementById('latitude').innerHTML = message.latitude;
    document.getElementById('longitude').innerHTML = message.longitude;
    document.getElementById('altitude').innerHTML = message.altitude;
    //gnss_listener.unsubscribe();
});

// Image data
var image_listener = new ROSLIB.Topic({
    ros: ros,
    name: '/d435/color/image_raw/compressed',
    messageType: 'sensor_msgs/CompressedImage'
});

image_listener.subscribe(function(message) {
    document.getElementById('my_image').src = "data:image/jpg;base64," + message.data;
    //image_listener.unsubscribe();
});

// Publishing a Topic
// ------------------

var cmd_vel = new ROSLIB.Topic({
    ros: ros,
    name: '/cmd_vel',
    messageType: 'geometry_msgs/Twist'
});

var twist = new ROSLIB.Message({
    linear: {
        x: 0.1,
        y: 0.2,
        z: 0.3
    },
    angular: {
        x: -0.1,
        y: -0.2,
        z: -0.3
    }
});
cmd_vel.publish(twist);