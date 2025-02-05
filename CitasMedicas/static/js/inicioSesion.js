window.document.addEventListener("DOMContentLoaded",iniciar);


function iniciar(){
    formularioEnviado();
}
let expUsuario = /^\w{2,}$/;
let expContrasenia =  /./;
function formularioEnviado(){
    let formulario = document.querySelector('form');
    formulario.addEventListener("submit",(evt)=>{
        evt.preventDefault();
        let inputs = formulario.querySelectorAll('input');
        if(expUsuario.test(inputs[0].value) && expContrasenia.test(inputs[1].value)){
            envioFormularioInicioSesion(inputs[0].value,inputs[1].value)
        }else{
            alerta("Error al leer campos","Introduce el usuario y contraseña","orange",2000);
        }
    })
}


async function envioFormularioInicioSesion(user,contrasenia){
    try{
        let resultado = await fetch("/loginUser?usuario="+ user + "&contrasenia="+contrasenia);
        if(!resultado) throw new Error("Ha ocurrido un problema en el inicio de sesión");
        let datos = await resultado.json();
        comprobacionInicioSesion(datos)
    }catch (error){
        console.log(error)
    }
}

function comprobacionInicioSesion(datos){
    if (datos.estado != false){
        alerta("Inicio de sesión correcto","Redirigiendo a la pagina principal","green",2000,redireccionHome);
    }else{
        alerta("Error de autentificación","El usuario o contraseña son incorrectos","red",2000);
    }
}
