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
    'storageBucket': "",
    'messagingSenderId': "495901667657",
    'appId': "1:495901667657:web:2629d55863304ef9"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def signIn(request):
    return render(request,"index.html")



def Logout(request):
    auth.logout(request)
    return render(request,"index.html")


def index(request):
    return render(request, 'index.html', {})

def registro(request):
    return render(request, 'register.html', {})

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
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid= user['localId']
        data={"name":name,"lastname":lastname,"status":"1"}
        database.child("users").child(uid).child("details").set(data)
        
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
    print(user['idToken'])

    session_id=user['idToken']
    request.session['uid']=str(session_id)

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    lol(a)



   
    asy = database.child('users').child(a).child('asignatura').child('asy').child('Asignatura1').get().val() 
    print(asy)

    return render(request, "load.html",{'asy':asy})





def lol(a):
    data = {
        "Asignatura1":"Lenguaje",
        "Asignatura2":"Matematicas",
        "Asignatura3":"Naturales",
        "Asignatura4":"Historia",
        "Asignatura5":"Ingles"
    }
    database.child('users').child(a).child('asignatura').child('asy').set(data)



# achiccar el codigo para que no se repita pero lo vere despues mientras lo are de la manera que no se debe
def comprobar(idtoken):

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print(idtoken)




def calendario(request):
    try:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print(idtoken)
    except:
        message="Dolor"
        return render(request,"index.html",{"messg":message})
    return render(request, 'calendario.html', {})


def micuenta(request):
    try:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print(idtoken)
        
    except:
        message="Dolor"
        return render(request,"index.html",{"messg":message})

    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request, 'micuenta.html', {'nombre':name})


def inicio(request):
    try:
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print(idtoken)
        
    except:
        message="Dolor"
        return render(request,"index.html",{"messg":message})
    
    asy = database.child('users').child(a).child('asignatura').child('asy').child('Asignatura1').get().val()
    return render(request, 'inicio.html', {'asy':asy})
  