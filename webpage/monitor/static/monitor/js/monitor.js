$(function() {
	var socket;

	var messaged = function(data) {
		alert(data.message);
	}   
        
	var start = function() {
		socket = new io.Socket();
		socket.connect();
		socket.on('connect', function () {
		    socket.subscribe('my channel');
		})
		socket.on('message', messaged);
	}
    
	start();
	socket.send("This is sent from the client upon connection");

});
