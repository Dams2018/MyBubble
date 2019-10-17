cuenta();
function cuenta(){
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            // User is signed in.
          var displayName = user.displayName;
          var email = user.email;
          var emailVerified = user.emailVerified;
          var photoURL = user.photoURL;
          var isAnonymous = user.isAnonymous;
          var uid = user.uid;
          var providerData = user.providerData;
          var datos = document.getElementById('datos');
          //probando mostrar datos desde firebase hacia html
          var verificado=""
          var boton

          switch(user.emailVerified) {
            case false:
                verificado="no"
                boton=`<a href="javascript:verificar(); mensaje();" class="btn btn-primary center">Verificar</a>`

              break;
            case true:
                verificado="si"
                boton=``
              break;
            default:
              // code block
          }

          datos.innerHTML = 
          `<div class="card center container-fluid temp" style="width: 30rem;">
          <img style='width:100px; height:100px' class="rounded-circle shadow center " 
          src="img/user.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title ">`+user.email+`</h5>
            <p class="card-text ">Tu cuenta `+verificado+` esta verificada.</p>`+boton+`

          </div>
        </div>`
          // ...
        } else {
          // User is signed out.
          // ...
        }
      });
}

function mensaje(){
    Swal.fire('Enviado correo ')
}