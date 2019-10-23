from django.shortcuts import render
from django.http import HttpResponse
from pyrebase import pyrebase
from django.contrib import auth
from django.contrib.auth import authenticate, logout, login


  


# Firebase
config = {
    'apiKey': "AIzaSyDr7sOBMFAeNZHS5W34TEvma_IzmJ4Dz80",
    'authDomain': "mybubblenet-326f3.firebaseapp.com",
    'databaseURL': "https://mybubblenet-326f3.firebaseio.com",
    'projectId': "mybubblenet-326f3",
    'storageBucket': "mybubblenet-326f3.appspot.com",
    'messagingSenderId': "495901667657",
    'appId': "1:495901667657:web:2629d55863304ef9"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
storage=firebase.storage()


def signIn(request):
    return render(request,"index.html")



def Logout(request):
    auth.logout(request)
    return render(request,"index.html")


def index(request):
    return render(request, 'index.html', {})

def registro(request):
    lista=["3ºBasico", "4ºBasico", "5ºBasico", "6ºBasico"]
    return render(request, 'register.html', {'asignaturas': lista})

def recover(request):
    return render(request, 'recover.html', {})


def recuperar(request):
    email=request.POST.get('email')
    authe.send_password_reset_email(email)
    return render(request, 'index.html', {})


    

def postsignup(request):
    name=request.POST.get('name')
    lastname=request.POST.get('lastname')
    email=request.POST.get('email')
    asignaturas=request.POST.get('asignatura')
    passw=request.POST.get('pass')

    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid= user['localId']
        data={"name":name,"lastname":lastname,"status":"1","asignatura":asignaturas}
        database.child("users").child(uid).child("detalles").set(data)

        
    except:
        message="La cuenta ya existe"
        return render(request,"index.html",{"messg":message})

    authe.send_email_verification(user['idToken'])
    return render(request,"index.html")





def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")

    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Error de Credencial"
        return render(request,"index.html",{"messg":message})
   # print(user['idToken'])

    session_id=user['idToken']
    request.session['uid']=str(session_id)

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    lol(a)
    cal(a)


    return render(request, "load.html",{})





def lol(a):

    asyg = database.child('users').child(a).child('detalles').child('asignatura').get().val()
    print(asyg)
    if asyg=="3ºBasico":
            data = {
        "Asignatura1":"Lenguaje",
        "Asignatura2":"Matemáticas",
        }
    elif asyg=="4ºBasico":
                    data = {
        "Asignatura1":"Lenguaje",
        "Asignatura2":"Matemáticas",
        "Asignatura3":"Naturales",
        }
    elif asyg=="5ºBasico":
                    data = {
        "Asignatura1":"Lenguaje",
        "Asignatura2":"Matemáticas",
        "Asignatura3":"Naturales",
        "Asignatura4":"Historia",
        }
    elif asyg=="6ºBasico":
                    data = {
        "Asignatura1":"Lenguaje",
        "Asignatura2":"Matemáticas",
        "Asignatura3":"Naturales",
        "Asignatura4":"Historia",
        "Asignatura5":"Inglés"
        }


    database.child('users').child(a).child('asignatura').child('asy').set(data)



# achiccar el codigo para que no se repita pero lo vere despues mientras lo are de la manera que no se debe
def comprobar():

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']





def calendario(request):
    try:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
    except:
        message="Tu sesión ha expirado."
        return render(request,"index.html",{"messg":message})

    img_url = database.child('users').child(a).child('imagen').child('url').get().val()
    #cal(a)
    lunes = database.child('users').child(a).child('calendario').child('01Lunes').get()
    martes = database.child('users').child(a).child('calendario').child('02Martes').get()
    miercoles = database.child('users').child(a).child('calendario').child('03Miercoles').get()
    jueves = database.child('users').child(a).child('calendario').child('04Jueves').get()
    viernes = database.child('users').child(a).child('calendario').child('05Viernes').get()
    semana = database.child('users').child(a).child('calendario').get()

    mlunes = []
    mmartes = []
    mmiercoles = []
    mjueves = []
    mviernes = []
    msemana = []

    for a in lunes.each():
        mlunes.append(a.val)

    for b in martes.each():
        mmartes.append(b.val)

    for c in miercoles.each():
        mmiercoles.append(c.val)

    for d in jueves.each():
        mjueves.append(d.val)

    for e in viernes.each():
        mviernes.append(e.val)
        
    for sem in semana.each():
        #print(sem.key()[2:]) #eliminando los
        msemana.append(sem.key()[2:])
       


    return render(request, 'calendario.html', {'img':img_url,'lunes':mlunes,'martes':mmartes,'miercoles':mmiercoles,
    'jueves':mjueves,'viernes':mviernes,'semana':msemana})



def cal(a):
    cali = database.child('users').child(a).child('calendario').get()


    lunes = {"0":"Matemáticas",
            "1":"Naturales",
            "2":"Inglés",
            "3":"Lenguaje"
            
            }
    database.child('users').child(a).child('calendario').child('01Lunes').set(lunes)
    martes = {"0":"Matemáticas",
            "1":"Historia"
            }
    database.child('users').child(a).child('calendario').child('02Martes').set(martes)
    miercoles = {"0":"Inglés",
            "1":"Historia"
            }
    database.child('users').child(a).child('calendario').child('03Miercoles').set(miercoles)
    jueves = {"0":"Matemáticas",
            "1":"Naturales",
            "2":"Inglés"
            }
    database.child('users').child(a).child('calendario').child('04Jueves').set(jueves)
    viernes = {"0":"Matemáticas",
            "1":"Naturales"
            }
    database.child('users').child(a).child('calendario').child('05Viernes').set(viernes)

def micuenta(request):
    try:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        
    except:
        message="Tu sesión ha expirado."
        return render(request,"index.html",{"messg":message})


        #datos de la cuenta
    #storage.child("images/customFile.jpg").put("customFile", user['idToken'])
    storage.child("images/customFile")

    asyg = database.child('users').child(a).child('detalles').child('asignatura').get().val()
    name = database.child('users').child(a).child('detalles').child('name').get().val()
    img_url = database.child('users').child(a).child('imagen').child('url').get().val()
    return render(request, 'micuenta.html', {'nombre':name,'asyg':asyg,'img':img_url})


def inicio(request):
    try:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        #print(idtoken)
        
    except:
        message="Tu sesión ha expirado."
        return render(request,"index.html",{"messg":message})
    
    asy = database.child('users').child(a).child('asignatura').child('asy').get()
    my_list = []
    for user in asy.each():
       # print(user.key()) # Asignatura
        #print(user.val()) # nombre se asignatura
        my_list.append(user.val())
    #print(my_list)   
    img_url = database.child('users').child(a).child('imagen').child('url').get().val()
    return render(request, 'Inicio.html', {'asy': my_list,'img':img_url})
  

def updateDatos(request):


    try:
        url = request.POST.get('url')
        idtoken= request.session['uid']
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
    except:
        message="Tu sesión ha expirado."
        return render(request,"index.html",{"messg":message})


    data = {
    'url':url
    }
    asyg = database.child('users').child(a).child('detalles').child('asignatura').get().val()
    name = database.child('users').child(a).child('detalles').child('name').get().val()
    database.child('users').child(a).child('imagen').set(data)
    img_url = database.child('users').child(a).child('imagen').child('url').get().val()
    print(img_url)
    return render(request, 'micuenta.html', {'nombre':name,'asyg':asyg,'img':img_url})
