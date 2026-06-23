from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('secretaire', 'Secrétaire'),
        ('agent', 'Agent'),
        ('directeur', 'Directeur'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='agent')
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.role}"

class Expediteur(models.Model):
    nom = models.CharField(max_length=150)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    organisation = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nom

class Destinataire(models.Model):
    nom = models.CharField(max_length=150)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    organisation = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nom

class Courrier(models.Model):
    TYPE_CHOICES = [
        ('entrant', 'Courrier entrant'),
        ('sortant', 'Courrier sortant'),
        ('interne', 'Courrier interne'),
    ]

    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('traite', 'Traité'),
        ('archive', 'Archivé'),
    ]

    numero = models.CharField(max_length=50, unique=True)
    type_courrier = models.CharField(max_length=20, choices=TYPE_CHOICES)
    objet = models.CharField(max_length=255)
    reference = models.CharField(max_length=100, blank=True, null=True)
    date_courrier = models.DateField()
    date_reception = models.DateField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    fichier = models.FileField(upload_to='courriers/', blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES ,default='en_attente')

    expediteur = models.ForeignKey(
        Expediteur,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='courriers'
    )

    destinataire = models.ForeignKey(
        Destinataire,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='courriers'
    )

    cree_par = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='courriers_crees'
    )

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.numero} - {self.objet}"

class Affectation(models.Model):
    courrier = models.ForeignKey(
        Courrier,
        on_delete=models.CASCADE,
        related_name='affectations'
    )

    utilisateur = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name='affectations'
    )

    date_affectation = models.DateTimeField(auto_now_add=True)
    instruction = models.TextField(blank=True, null=True)
    traite = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['courrier', 'utilisateur'],
                name='unique_affectation_courrier_utilisateur'
            )
        ]

    def __str__(self):
        return f"{self.courrier.numero} -> {self.utilisateur.username}"