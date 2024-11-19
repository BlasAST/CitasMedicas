window.document.addEventListener("DOMContentLoaded", iniciar);


function iniciar() {
    formularioEnviado();
}

// Expresiones regulares para filtrar caracteres no deseados en el formulario
let expNombreYApellidos = /^[A-Za-z]{2,}( [A-Za-z])*/
let expDNI = /^[0-9]+[A-Za-z]{1}$/
let expFechaNacimiento = /^\d{4}-\d{2}-\d{2}$/
let expUsuario = /^\w{5,}$/
let expContrasenia = /^.{2,}$/

// Comprobación de los datos con las expresiones regulares
function formularioEnviado() {
    let formulario = document.querySelector('form');
    formulario.addEventListener("submit", (evt) => {
        evt.preventDefault();
        let inputs = formulario.querySelectorAll("input");
        let valores = [...inputs].map(valor => valor.value)
        if (valores[5] == valores[6]) {
            if (expNombreYApellidos.test(valores[0]) != false &&
                expNombreYApellidos.test(valores[1]) != false &&
                expDNI.test(valores[2]) != false &&
                expFechaNacimiento.test(valores[3]) != false &&
                expUsuario.test(valores[4]) != false &&
                expContrasenia.test(valores[5]) != false) {
                enviarFormulario(valores)
            } else console.log("Ha ocurrido un error");
        } else console.log("Las contraseñas no coinciden");
    })
}

async function enviarFormulario(valores) {
    try {
        let resultado = await fetch("/createUser?nombre=" + valores[0] +
            "&apellidos=" + valores[1] +
            "&dni=" + valores[2] +
            "&fechaNacimiento=" + valores[3] +
            "&usuario=" + valores[4] +
            "&contrasenia=" + valores[5]);
        if (!resultado) throw new Error("No se ha podido realizar la consulta")
        let datos = await resultado.json();
        console.log(datos);
    }
    catch (error) {
        console.error(error)
    }
}