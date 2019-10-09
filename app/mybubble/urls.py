from django.contrib import admin
from django.urls import path,include
from .views import index,registro,recover, signIn



urlpatterns = [
    path('', signIn, name="index"),
    path('registro', registro, name="registro"),
    path('recover', recover, name="recover"),
    
    

]

