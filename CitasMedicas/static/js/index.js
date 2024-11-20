window.addEventListener("DOMContentLoaded",iniciar)

function iniciar(){
    if(window.location.pathname=='/'){
        // Primera redireccion de la pagina de inicio a seleccion de
        // Inicio de sesión o registro
        redirecciones1();
    }
    if(window.location.pathname=='/logReg'){
        // Redireccion segun se pulse el boton de inicio de sesión o register
        // Las redirecciones de los formularios se realizan mediantes enlaces en html
        redirecciones2();
    }
    if(window.location.pathname=='/inicioSesion'){
        redirecciones3();
    }
    if(window.location.pathname=='/registrarse'){
        redirecciones4();
    }
}

function redirecciones1(){
    let botonIniReg = document.querySelector('.logReg')
    botonIniReg.addEventListener("click",()=>{
        window.location.href='/logReg';
    })
}

function redirecciones2(){
    let botones= document.querySelectorAll(".botones");
    botones[0].addEventListener("click",()=>{
        window.location.href="/inicioSesion";
    })
    botones[1].addEventListener("click",()=>{
        window.location.href="/registrarse";
    })
}


function redirecciones3(){
        
}


function redirecciones4(){

}


// Redireccion para llevar al portal cuando se ha realizado correctamente la autentificación
function redireccionHome(){
    window.location.href="/home";
}