from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur, Expediteur, Destinataire, Courrier, Affectation


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    search_fields = ("username", "first_name", "last_name", "email")

    fieldsets = UserAdmin.fieldsets + (
        ("Informations supplémentaires", {"fields": ("role", "telephone")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Informations supplémentaires", {"fields": ("role", "telephone")}),
    )


@admin.register(Expediteur)
class ExpediteurAdmin(admin.ModelAdmin):
    list_display = ("nom", "organisation", "telephone", "email")
    search_fields = ("nom", "organisation", "telephone", "email")


@admin.register(Destinataire)
class DestinataireAdmin(admin.ModelAdmin):
    list_display = ("nom", "organisation", "telephone", "email")
    search_fields = ("nom", "organisation", "telephone", "email")


@admin.register(Courrier)
class CourrierAdmin(admin.ModelAdmin):
    list_display = ("numero", "type_courrier", "objet", "statut", "date_courrier", "cree_par")
    list_filter = ("type_courrier", "statut", "date_courrier")
    search_fields = ("numero", "objet", "reference")


@admin.register(Affectation)
class AffectationAdmin(admin.ModelAdmin):
    list_display = ("courrier", "utilisateur", "date_affectation", "traite")
    list_filter = ("traite", "date_affectation")