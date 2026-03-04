//ve se ter id aviso na pagina
if (document.getElementById("aviso") === null) {
	console.log("Sem aviso");
} else {
	//id aviso some quando clicado
	document.getElementById("aviso").addEventListener("click", function() {
		document.getElementById("aviso").style.opacity = "0";
		document.getElementById("aviso").style.transition = "opacity 0.3s";
		setTimeout(function() {document.getElementById("aviso").style.display = "none";}, 1000);
	});
}
const notas = document.querySelectorAll(".nota");
notas.forEach(nota => {
    nota.addEventListener("mousedown", function(e) {
        const offsetX = e.clientX - nota.offsetLeft;
        const offsetY = e.clientY - nota.offsetTop;

        function mover(e) {
            nota.style.left = e.clientX - offsetX + "px";
            nota.style.top = e.clientY - offsetY + "px";
        }

        document.addEventListener("mousemove", mover);

        document.addEventListener("mouseup", () => {
            document.removeEventListener("mousemove", mover);
        }, { once: true });
    });
});
