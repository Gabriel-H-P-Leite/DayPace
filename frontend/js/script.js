//id aviso some quando clicado
document.getElementById("aviso").addEventListener("click", function() {
	document.getElementById("aviso").style.opacity = "0";
	document.getElementById("aviso").style.transition = "opacity 0.3s";
	setTimeout(function() {document.getElementById("aviso").style.display = "none";}, 1000);
});
