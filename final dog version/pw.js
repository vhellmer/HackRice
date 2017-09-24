function new_event() {

    var event = document.getElementById("event").value;
    var day = document.getElementById("day").value;
    var time = document.getElementById("time").value
    var dayTime = day.concat(time)
    
    document.getElementById(dayTime).innerHTML = event;
}
function cancel_event(){
	var day = document.getElementById("day").value;
    var time = document.getElementById("time").value
    var dayTime = day.concat(time)
    
    document.getElementById(dayTime).innerHTML = "";
}
