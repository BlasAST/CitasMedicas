window.addEventListener("DOMContentLoaded",iniciar)

function iniciar(){
    if(window.location.pathname=='/'){
        redirecciones1();
    }
    if(window.location.pathname=='/logReg'){
        redirecciones2();
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
        window.location.href=("/inicioSesion")
    })
    botones[1].addEventListener("click",()=>{
        window.location.href=("/registrarse")
    })
}