window.document.addEventListener("DOMContentLoaded",iniciar);


function iniciar(){
    formularioEnviado();
}
let expUsuario = '/w{5,}/';
let expContrasenia =  '/./';
function formularioEnviado(){
    let formulario = document.querySelector('form');
    formulario.addEventListener("submit",(evt)=>{
        evt.preventDefault();
        let inputs = formulario.querySelectorAll('input');
    })
}