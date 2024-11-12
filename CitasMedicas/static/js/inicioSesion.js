window.document.addEventListener("DOMContentLoaded",iniciar);


function iniciar(){
    formularioEnviado();
}

function formularioEnviado(){
    let formulario = document.querySelector('form');
    formulario.addEventListener("submit",(evt)=>{
        evt.preventDefault();

    })
}