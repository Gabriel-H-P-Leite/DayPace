//cookie
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
//Fechar
//ve se tem fechar
if (document.querySelectorAll(".fechar") === null) {
	console.log("Sem fechar");
} else {
	document.querySelectorAll(".fechar").forEach(botao => {
		botao.addEventListener("click", function(){
			this.parentElement.style.opacity = "0";
			this.parentElement.style.transition = "opacity 0.3s";
			setTimeout(() => { this.parentElement.style.display = "none"; }, 300);
		});
	});
}
//moverTarefa
moveTarefa = null;
document.querySelectorAll(".nota").forEach(nota => {
	nota.addEventListener("dragstart", function() {
		moveTarefa = this
	})
})
document.querySelectorAll(".coluna").forEach(coluna => {

	coluna.addEventListener("dragover", function(e){
	e.preventDefault()
	})

	coluna.addEventListener("drop", function(){
		if(moveTarefa){
			this.appendChild(moveTarefa)
			const id = moveTarefa.dataset.id
			const status = this.dataset.status
			fetch("/tarefa/mover/", {
				method: "POST",
				headers:{
					"Content-Type":"application/json",
					"X-CSRFToken": getCookie("csrftoken")
				},
				body: JSON.stringify({
					id:id,
					status:status
				})
			})
		}
	})
})
let arrastando = null;
document.querySelectorAll(".tarefa").forEach(nota => {
	nota.addEventListener("dragstart", function(){
		arrastando = this;
	});
	nota.addEventListener("dragover", function(e){
		e.preventDefault();
	});
	nota.addEventListener("drop", function(){
		let idArrastado = arrastando.dataset.id;
		let idAlvo = this.dataset.id;
		// mover visualmente
		this.parentNode.insertBefore(arrastando, this);
		// enviar para backend
		fetch(`/tarefa/prioridade/`,{
			method:"POST",
			headers:{
				"Content-Type":"application/json",
				"X-CSRFToken": csrftoken
			},
			body:JSON.stringify({
				tarefa: idArrastado,
				acima_de: idAlvo
			})
		});
	});
});
