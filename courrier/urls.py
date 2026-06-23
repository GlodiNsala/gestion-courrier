from django.urls import path, include # path cree les routes, include importe les routes d'une app
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin # Importe l'administration Django


urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("courriers/", views.liste_courriers, name="liste_courriers"),
    path("courriers/ajouter/", views.ajouter_courrier, name="ajouter_courrier"),
    path("expediteurs/ajouter/", views.ajouter_expediteur, name="ajouter_expediteur"),
    path("destinataires/ajouter/", views.ajouter_destinataire, name="ajouter_destinataire"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="courrier/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    path("courriers/<int:pk>/", views.detail_courrier, name="detail_courrier"),
    path("courriers/<int:pk>/modifier/", views.modifier_courrier, name="modifier_courrier"),
    path("courriers/<int:pk>/supprimer/", views.supprimer_courrier, name="supprimer_courrier"),
]