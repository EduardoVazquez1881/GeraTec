"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from geraGames import views
from django.conf import settings
from django.conf.urls.static import static


from geraGames.models import Usuario, Categoria, Plataforma, Creador, Juego, Review, JuegosDatos



urlpatterns = [
    path('admin/', admin.site.urls),
    path("prueba/", views.prueba),
    path("info/", views.info),
    path("login/", views.login),
    path("menu/", views.menu, name='menu'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
