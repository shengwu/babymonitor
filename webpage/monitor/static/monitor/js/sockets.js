$(function() {
	var socket;
	var channel = 'default-channel';
	var messaged = function(data) {
        if(data.message){
		    alert(data.message);
        }
	}   
        
	var start = function() {
		socket = new io.Socket();
		socket.connect();
		socket.on('connect', function () {
		    socket.subscribe(channel);
		})
		socket.on('message', messaged);
	}
    
	start();
	socket.send(channel);
});
