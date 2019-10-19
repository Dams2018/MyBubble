
hideAddressBar();
//hola


function hideAddressBar()
{
  if(!window.location.hash)
  {
      if(document.height < window.outerHeight)
      {
          document.body.style.height = (window.outerHeight + 50) + 'px';
      }

      setTimeout( function(){ window.scrollTo(0, 1); }, 50 );
  }
}

window.addEventListener("load", function(){ if(!window.pageYOffset){ hideAddressBar(); } } );
window.addEventListener("orientationchange", hideAddressBar );



function reg(){
    var email = document.getElementById('email').value;
    var pass = document.getElementById('pass').value;
    console.log(email)

    firebase.auth().createUserWithEmailAndPassword(email, pass)
    .then(function(){
      verificar()
    })

    .catch(function(error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        console.log(errorCode)

        switch(errorCode) {
            case "auth/invalid-email":
                Swal.fire({
                    type: 'error',
                      title: 'Oops...',
                       text: 'El campo del correo está vacío o es invalido',
                     }) 
              break;
            case "auth/wrong-password":
                Swal.fire({
                    type: 'error',
                      title: 'Oops...',
                       text: 'Contraseña vacia o invalida',
                     }) 
              break;
            case "auth/weak-password":
                    Swal.fire({
                        type: 'error',
                          title: 'Oops...',
                           text: 'Contraseña debe ser igual o mas de 6 caracteres',
                         }) 
              break;
            default:
              // code block
          }
        // ...
      });
}

function ingre(){
  console.log("boton")
    var email2 = document.getElementById('email').value;
    var pass2 = document.getElementById('pass').value;


    firebase.auth().signInWithEmailAndPassword(email2, pass2)
    .catch(function(error) {

        
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        console.log(errorCode)


        switch(errorCode) {
            case "auth/invalid-email":
                Swal.fire({
                    type: 'error',
                      title: 'Oops...',
                       text: 'El campo del correo está vacío o es invalido',
                     }) 
              break;
            case "auth/wrong-password":
                Swal.fire({
                    type: 'error',
                      title: 'Oops...',
                       text: 'Contraseña vacia o invalida',
                     }) 
              break;
            default:
              // code block
          }

      });
}



function loageado(){
    var contenido = document.getElementById('logeado');
    contenido.innerHTML = `<META HTTP-EQUIV="REFRESH" CONTENT="1;URL=inicio.html">`
}

function desloageado(){
    var contenido = document.getElementById('desloageado');
    contenido.innerHTML = `<META HTTP-EQUIV="REFRESH" CONTENT="1;URL=index.html">`
}

function cerrar(){
    firebase.auth().signOut()
    .then(function(){
        console.log('saliendo')
    })
    .catch(function(error){
        console.log(error)
    })
}


function salir(){

    Swal.fire({
        type: 'success',
        title: 'Saliendo',
        showConfirmButton: false,
        timer: 1500
      }).then(()=> {
      
        this.cerrar(); 
        this.desloageado();// this should execute now
      
      })


}

function verificar(){
  var user = firebase.auth().currentUser;

user.sendEmailVerification().then(function() {
  // Email sent.
}).catch(function(error) {
  // An error happened.
});
}


//barra no usando

$(function() {
    var current_progress = 0;
    var interval = setInterval(function() {
        current_progress += 1;
        $("#dynamic")
        .css("width", current_progress + "%")
        .attr("aria-valuenow", current_progress)
        .text(current_progress + "% Completado");
        if (current_progress >= 100)
            clearInterval(interval);
    }, 50);
});


//Seccion de preguntas


function error(){
  Swal.fire({
    type: 'error',
    title: 'Error!',
    text: 'No puedes dejar las respuestas en blanco!',
    timer: 1600,
    showConfirmButton: false
  })
  
}
function Aprueba(resultado){
  Swal.fire(
    'Quiz Guardado Tienes '  + resultado + ' Respuestas correctas' ,
    'respuestas enviadas!' + 'Tienes ',
    'success',
  )
}
function calcular(){
 
  if (! $("input[name=one]").is(":checked") || ! $("input[name=two").is(":checked") ) {
    error();    
    return;  
  } 
  
  var resultado = 0;
  var a,b;
  var valorOne = document.getElementsByName("one");
  for (let i = 0; i < valorOne.length; i++) {
      if (valorOne[i].checked) {

        a = parseInt(valorOne[i].value);
        console.log("a = "+a);
      }
  }
  var valorTwo = document.getElementsByName("two");
  for (let i = 0; i < valorTwo.length; i++) {
    if (valorTwo[i].checked) {

      b = parseInt(valorTwo[i].value);
      console.log("b = "+b);
    }
}
/* Limpiar radiobuttons */  
var ele = document.getElementsByName("one");
   for(var i=0;i<ele.length;i++){
     ele[i].checked = false;
    }

    var ele = document.getElementsByName("two");
   for(var i=0;i<ele.length;i++){
     ele[i].checked = false;
    }

      
resultado =  a + b; 
console.log("Resultado :"+resultado);
Aprueba(resultado);

}


function redireccionar() {
  setTimeout("location.href='bubble.html'", 5000);}

//comunidad












