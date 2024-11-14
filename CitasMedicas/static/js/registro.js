window.document.addEventListener("DOMContentLoaded",iniciar);


function iniciar(){
    formularioEnviado();
    console.log("holi")
}


let expNombreYApellidos= "/[A-Za-z]{2,}/"
let expDNI= "/[0-9]+[A-Za-z]{1}/"
let expFechaNacimiento= "/\d{2}-\d{2}-\d{4}/"
let expUsuario= "/\w{5,}/"
let expContrasenia= "/./"
let expContrasenia2= "/./"

function formularioEnviado(){
    let formulario = document.querySelector('form');
    formulario.addEventListener("submit",(evt)=>{
        evt.preventDefault();
        let inputs = formulario.querySelectorAll("input");
    })
}