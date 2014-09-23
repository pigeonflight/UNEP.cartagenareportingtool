$(document).ready(function() {
	var logoutbtn = document.createElement("a");
	var t = document.createTextNode("log out");
	logoutbtn.appendChild(t);
	var header = document.querySelector("header");
	header.appendChild(logoutbtn);
	logoutbtn.href = "logout";
	logoutbtn.className = "btn btn-warning logout-btn";
});