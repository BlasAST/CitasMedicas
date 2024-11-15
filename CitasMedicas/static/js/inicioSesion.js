window.document.addEventListener("DOMContentLoaded",iniciar);


function iniciar(){
    formularioEnviado();
}
let expUsuario = /^\w{5,}$/;
let expContrasenia =  /./;
function formularioEnviado(){
    let formulario = document.querySelector('form');
    formulario.addEventListener("submit",(evt)=>{
        evt.preventDefault();
        let inputs = formulario.querySelectorAll('input');
        if(expUsuario.test(inputs[0].value) && expContrasenia.test(inputs[1].value)){
            envioFormularioInicioSesion(inputs[0].value,inputs[1].value)
        }
    })
}


async function envioFormularioInicioSesion(user,contrasenia){
        let resultado = await fetch("/loginUser?usuario="+ user + "&contrasenia="+contrasenia);
        if(!resultado) throw new Error("Ha ocurrido un problema en el inicio de sesión");
        console.log(resultado)
        // let datos= await resultado.json();
        // comprobacionInicioSesion(datos);
}


function comprobacionInicioSesion(datos){
    console.log(datos);
}