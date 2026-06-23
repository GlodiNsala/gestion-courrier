from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CourrierForm, ExpediteurForm, DestinataireForm
from .models import Courrier
from .decorators import role_required # Importe notre decorateur de verification des roles

# Create your views here.
@login_required
def accueil(request):
    # Tout utilisateur connecte peut voir l'accueil.

    return render(request, "courrier/accueil.html")

@login_required
def liste_courriers(request):
    # Tout utilisateur connecte peut voir la liste.

    courriers = Courrier.objects.all()
    return render(request, "courrier/liste_courriers.html", {"courriers": courriers})

@login_required
@role_required("admin", "secretaire")
# Seuls admin et secretaire peuvent ajouter un expediteur.

def ajouter_expediteur(request):
    if request.method == "POST":
        form = ExpediteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ajouter_courrier")
    else:
        form = ExpediteurForm()

    return render(request, "courrier/form.html", {
        "form": form,
        "titre": "Ajouter un expéditeur"
    })

@login_required
@role_required("admin", "secretaire")
    # Seuls admin et secretaire peuvent ajouter un destinataire.

def ajouter_destinataire(request):
    if request.method == "POST":
        form = DestinataireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ajouter_courrier")
    else:
        form = DestinataireForm()

    return render(request, "courrier/form.html", {
        "form": form,
        "titre": "Ajouter un destinataire"
    })


@login_required
@role_required("admin", "secretaire")
# Seuls admin et secretaire peuvent ajouter un courrier.

def ajouter_courrier(request):
    if request.method == "POST":
        form = CourrierForm(request.POST, request.FILES)
        if form.is_valid():
            courrier = form.save(commit=False)
            courrier.cree_par = request.user
            courrier.save()
            return redirect("liste_courriers")
    else:
        form = CourrierForm()

    return render(request, "courrier/form.html", {
        "form": form,
        "titre": "Ajouter un courrier"
    })


@login_required
def detail_courrier(request, pk):
    # Tout utilisateur connecte peut voir le detail.
    # On cherche un courrier avec son id.
    # Si le courrier n'existe pas, Django affiche une erreur 404
    courrier = get_object_or_404(Courrier, pk=pk)

    # On affiche la page de détail avec le courrier trouvé.
    return render(request, "courrier/detail_courrier.html",{
        "courrier": courrier
    })


@login_required
@role_required("admin", "secretaire")
    # Seuls admin et secretaire peuvent modifier un courrier.

def modifier_courrier(request, pk):
    # On récupère le courrier à modifier.
    courrier = get_object_or_404(Courrier, pk=pk)

    # Si l'utilisateur envoie le formulaire.
    if request.method == "POST":
        # On remplit le formulaire avec les nouvelles données.
        # instance=courrier veut dire : modifier ce courrier, ne pas en créer un nouveau.
        form = CourrierForm(request.POST, request.FILES, instance=courrier)

        # Si les données sont valides.
        if form.is_valid():
            # On sauvegarde les modifications.
            form.save()

            # Après modification, on retourne à la liste des courriers.
            return redirect("liste_courriers")

    else:
        # Si l'utilisateur ouvre seulement la page, on affiche le formulaire déjà rempli.
        form = CourrierForm(instance=courrier)

    # On affiche le formulaire de modification.
    return render(request, "courrier/form.html", {
        "form": form,
        "titre": "Modifier un courrier"
    })


@login_required
@role_required("admin")
    # Seul admin peut supprimer un courrier.

def supprimer_courrier(request, pk):
    # On récupère le courrier à supprimer.
    courrier = get_object_or_404(Courrier, pk=pk)

    # Si l'utilisateur confirme la suppression.
    if request.method == "POST":
        # On supprime le courrier de la base de données.
        courrier.delete()

        # Après suppression, on retourne à la liste.
        return redirect("liste_courriers")

    # Si l'utilisateur ouvre seulement la page, on affiche une confirmation.
    return render(request, "courrier/confirm_delete.html", {
        "courrier": courrier
    })


