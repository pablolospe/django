/////////////////////////////////
// VALIDACIONES DEL FORMULARIO //
/////////////////////////////////

const nombre = document.getElementById('nombre');
const email = document.getElementById('email');
const asunto = document.getElementById('asunto');
const mensaje = document.getElementById('mensaje');
const parrafo = document.getElementById('warnings');

form.addEventListener("submit", (e)=>{
    e.preventDefault();
    let warnings = ''
    let regexEmail = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
    let entrar = false
    parrafo.innerHTML = ''
    if(nombre.value.length <3){
        warnings += `El nombre debe poseer al menos 3 caracteres <br>`
        entrar = true
    }
    if(!regexEmail.test(email.value)){
        warnings += `Debe ingresar un email válido <br>`
        entrar = true
    }
    if(asunto.value.length < 1){
        warnings += `Debe ingresar un asunto <br>`
        entrar = true
    }
    if(mensaje.value.length < 1){
        warnings += `Debe ingresar un mensaje <br>`
        entrar = true
    }
    if(entrar){
        parrafo.innerHTML = warnings;
    } else {
        form.submit();
    }
})