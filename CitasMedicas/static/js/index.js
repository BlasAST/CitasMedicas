window.addEventListener("DOMContentLoaded",iniciar)

function iniciar(){
    if(window.location.pathname=='/'){
        // Primera redireccion de la pagina de inicio a seleccion de
        // Inicio de sesión o registro
        redirecciones1();
        cambiarFondo();
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

function cambiarFondo(){
    let botones = document.querySelector(".fondo");
    let header = document.querySelector(".header");
    let container = document.querySelector(".container");
    console.log(botones.firstElementChild)
    console.log(header,container);

    botones.lastElementChild.addEventListener("click",()=>{
        botones.lastElementChild.classList.toggle("activo");
        botones.firstElementChild.classList.toggle("activo");
        header.classList.toggle("dark");
        container.classList.toggle("white");
        container.classList.toggle("dark");
    })
    botones.firstElementChild.addEventListener("click",()=>{
        botones.firstElementChild.classList.toggle("activo");
        botones.lastElementChild.classList.toggle("activo");
        header.classList.toggle("white");
        container.classList.toggle("white");
        container.classList.toggle("dark");
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

function alerta(cabecera,mensaje,color,tiempo,funcion){
    let alerta= document.querySelector('.alerta');
    alerta.style.backgroundColor=color;
    let cabeza=alerta.querySelector(":first-child");
    cabeza.textContent="";
    cabeza.appendChild(document.createTextNode(cabecera));
    let mesage= alerta.querySelector(":last-child");
    mesage.textContent="";
    mesage.appendChild(document.createTextNode(mensaje));
    alerta.style.display="flex";
    setTimeout(()=>{alerta.style.display="none";if(funcion) funcion();},tiempo);
    
}