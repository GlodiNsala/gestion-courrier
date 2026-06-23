from functools import wraps # Permet de creer proprement un decorateur Python
from django.shortcuts import redirect # Permet de rediriger l'utilisateur vers une autre page
from django.contrib import messages # Permet d'afficher un message a l'utilisateur


def role_required(*roles):
    # Cette fonction recoit une liste de roles autorises.
    # Exemple : @role_required("admin", "secretaire")

    def decorator(view_func):
        # decorator recoit la vue Django a proteger.


        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # wrapper est la fonction qui serq executee avant la vraie vue.

            if not request.user.is_authenticated:
                # Si l'utilisateur n'est pas connecte,
                # on le redirige vers la page de connexion.
                return redirect("login")

            if request.user.is_superuser:
                # Si l'utilisateur est superuser Django
                # on l'autorise toujours.
                return view_func(request, *args, **kwargs)

            if request.user.role not in roles:
                # Si le rôle de l'utilisateur n'est pas dans les rôles autorisés,
                # on bloque l'action.
                messages.error(request, "Vous n'avez pas l'autorisation d'effectuer cette action.")

                # On renvoie l'utilisateur vers la liste des courriers.
                return redirect("liste_courriers")

            # Si tout est correct, on exécute normalement la vue demandée.
            return view_func(request, *args, **kwargs)

        return wrapper
    
    return decorator