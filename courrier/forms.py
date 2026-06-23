from django import forms
from .models import Courrier, Expediteur, Destinataire


class DateInput(forms.DateInput):
    input_type = "date"


class ExpediteurForm(forms.ModelForm):
    class Meta:
        model = Expediteur
        fields = ["nom", "adresse", "telephone", "email", "organisation"]

class DestinataireForm(forms.ModelForm):
    class Meta:
        model = Destinataire
        fields = ["nom", "adresse", "telephone", "email", "organisation"]

class CourrierForm(forms.ModelForm):
    class Meta:
        model = Courrier
        fields = [
            "numero",
            "type_courrier",
            "objet",
            "reference",
            "date_courrier",
            "date_reception",
            "resume",
            "fichier",
            "statut",
            "expediteur",
            "destinataire",
        ]
        widgets = {
            "date_courrier": DateInput(),
            "date_reception": DateInput(),
            "resume": forms.Textarea(attrs={"rows": 4}),
        }