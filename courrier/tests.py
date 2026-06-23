
from django.test import TestCase # Class utilisée pour écrire des tests Django
from django.urls import reverse # Permet de retrouver une URL a partir de son nom
from django.contrib.auth import get_user_model # Récupère ton modèle utilisateur personnalisé

from .models import Courrier # Importe le modèle Courrier
# Create your tests here.



class CourrierModelTest(TestCase):
    # Cette classe teste le modèle Courrier

    def setUp(self):
        # setUp est exécuté avant chaque test.
        # On y prépare les données nécessaires.

        User = get_user_model()
        # Récupère le modele Utilisateur defini par AUTH_USER_MODEL

        self.user = User.objects.create_user(
            username="admin_test",
            password="test12345",
            role="admin",
        )
        # Cree un utilisateur de test dans la base de test

    def test_creation_courrier(self):
        # Ce test verifie qu'on peut creer un courrier

        courrier = Courrier.objects.create(
            numero="C-001",
            type_courrier="entrant",
            objet="Test courrier",
            date_courrier="2026-06-12",
            statut="en_attente",
            cree_par=self.user,
        )
        # Cree un courrier dans la base de test

        self.assertEqual(courrier.numero, "C-001")
        # Verifie que le numero enregistre est correct

        self.assertEqual(str(courrier), "C-001 - Test courrier")
        # Verifie que __str__ affiche bien le courrier


class ConnexionTest(TestCase):
    # Cette classe teste la connexion utilisateur

    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="agent_test",
            password="test12345",
            role="agent",
        )

    def test_login_page_accessible(self):
        # Verifie que la page login s'ouvre

        response = self.client.get(reverse("login"))
        # Simule une visite sur la page login

        self.assertEqual(response.status_code, 200)
        # 200 veut dire : la page s'affiche correctement

    def test_user_can_login(self):
        # Verifie qu'un utilisateur peut se connecter

        login_success = self.client.login(
            username="agent_test",
            password="test12345",
        )
        # Essaie de connecter l'utilisateur

        self.assertTrue(login_success)
        # Verifie que la connexion a reussi


class CourrierViewTest(TestCase):
    # Cette classe teste les pages liees aux courries

    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="admin_test",
            password="test12345",
            role="admin",
        )

    def test_liste_courriers_requires_login(self):
        # Verifie qu'un utilisateur non connecte est redirige vers login

        response = self.client.get(reverse("liste_courriers"))
        # Essaie d'ouvrir la liste sans etre connecte

        self.assertEqual(response.status_code, 302)
        # 302 veut dire : redirection

    def test_liste_courriers_connected_user(self):
        # Verifie qu'un utilisateur connecte peut voir la liste

        self.client.login(username="admin_test", password="test12345")
        # Connecte l'utilisateur

        response = self.client.get(reverse("liste_courriers"))
        # Ouvre la page liste des courriers

        self.assertEqual(response.status_code, 200)
        # Verifie que la page s'affiche correctement