window.document.addEventListener("DOMContentLoaded",iniciar);


function iniciar(){
    formularioEnviado();
    console.log("Hola?")
}

function formularioEnviado(){
    let boton = document.querySelector('#submit');
    boton.addEventListener("click",(evt)=>{
        evt.preventDefault();
        
    })
}