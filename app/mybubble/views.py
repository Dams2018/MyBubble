from django.shortcuts import render
from django.http import HttpResponse
from pyrebase import pyrebase
from django.contrib import auth


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


    name = database.child('users').child(a).child('details').child('name').get().val()
    asy = database.child('users').child(a).child('asignatura').child('asy').child('Asignatura1').get().val() 
    print(asy)
    return render(request, "inicio.html",{"e":email,'i':name,'asy':asy})





def lol(a):
    data = {
        "Asignatura1":"Lenguaje",
        "Asignatura2":"Matematicas",
        "Asignatura3":"Naturales",
        "Asignatura4":"Historia",
        "Asignatura5":"Ingles"
    }
    database.child('users').child(a).child('asignatura').child('asy').set(data)


def calendario(request):
    return render(request, 'calendario.html', {})
