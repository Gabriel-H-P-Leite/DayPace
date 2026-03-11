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

let tarefaId = null;

document.querySelectorAll(".nota").forEach(nota => {

    nota.addEventListener("dragstart", function() {
        tarefaId = this.dataset.id
    })

})


document.querySelectorAll(".coluna").forEach(coluna => {

    coluna.addEventListener("dragover", function(e){
        e.preventDefault()
    })

    coluna.addEventListener("drop", function(){

        const status = this.dataset.status

        fetch("/tarefa/mover/", {
            method: "POST",
            headers:{
                "Content-Type":"application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({
                id: tarefaId,
                status: status
            })
        })

    })

})
function getCookie(name) {
let cookieValue = null;
if (document.cookie && document.cookie !== '') {
const cookies = document.cookie.split(';');
for (let i = 0; i < cookies.length; i++) {
const cookie = cookies[i].trim();
if (cookie.substring(0, name.length + 1) === (name + '=')) {
cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
break;
}
}
}
return cookieValue;
}
