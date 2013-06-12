$(function() {
	var socket;
	var channel = 'default-channel';
	var messaged = function(data) {
        if(data.message){
		    alert(data.message);
        }
	};
        
	var start = function() {
		socket = new io.Socket();
        console.log(socket);
        for (var attr in socket) {
            console.log(attr);
        }
		socket.connect();
		socket.on('connect', function() {
		    socket.subscribe(channel);
		});
		socket.on('message', messaged);
	};
    
	start();
	socket.send(channel);
});
