"""
URL configuration for gestion_courrier project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include # path cree les routes, include importe les routes d'une app
from django.conf import settings # Permet d'acceder aux variables de settings.py
from django.conf.urls.static import static # Permet de servir les fichiers medias en developpement
from django.views.defaults import server_error
from courrier import views

urlpatterns = [
    path('admin/', admin.site.urls), # Route vers l'administration Django
    path("", include("courrier.urls")), # Route principale vers les URLs de l'application courrier
]

if settings.DEBUG:
    # Cette condition veut dire : seulement quand DEBUG=True.
    # Donc uniquement en developpement, pas en production.

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # MEDIA_URL correspond a l'adresse web des fichiers, par exemple /media/
    # MEDIA_ROOT correspond au dossier reel ou les fichiers sont stockes