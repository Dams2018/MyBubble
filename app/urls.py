"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from mybubble import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('',include('mybubble.urls')),
    path('postsign/',views.postsign),
    path('recover/',views.recover),
    path('logout/',views.Logout, name="log"),
    path('register/',views.registro, name='signup'),
    path('postsignup/',views.postsignup, name='postsignup'),
    path('calendario/',views.calendario, name='calendario'),
    path('micuenta/',views.micuenta, name='micuenta'),
    path('inicio/',views.inicio, name='inicio'),
    path('recuperar/',views.recuperar, name='recuperar'),
    path('updateDatos/',views.updateDatos, name='updateDatos'),  
    path('bubble/',views.bubble, name='bubble'),  
    

       
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
