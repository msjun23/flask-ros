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
var gnssTopic = new ROSLIB.Topic({
    ros: ros,
    name: '/gnss',
    messageType: 'sensor_msgs/NavSatFix'
});

gnssTopic.subscribe(function(message) {
    console.log('Received message on ' + gnssTopic.name + ': ' + message.latitude + ', ' + message.longitude + ', ' + message.altitude);
    document.getElementById('latitude').innerHTML = message.latitude;
    document.getElementById('longitude').innerHTML = message.longitude;
    document.getElementById('altitude').innerHTML = message.altitude;
    //gnssTopic.unsubscribe();
});

// Image data
var imageTopic = new ROSLIB.Topic({
    ros: ros,
    name: '/d435/color/image_raw/compressed',
    messageType: 'sensor_msgs/CompressedImage'
});

imageTopic.subscribe(function(message) {
    document.getElementById('my_image').src = "data:image/jpg;base64," + message.data;
    //imageTopic.unsubscribe();
});