from datetime import date
from django.db import models

# Create your models here.
class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100)

    def __str__(self):
        return self.nomCat

class Statut(models.Model):
    idStatut = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=200)

    def __str__(self):
        return self.libelle
    
class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    dateFabrication = models.DateField(default=date.today)

    # Relation CIF : chaque produit appartient à 1 catégorie (0,N côté catégorie → 1,1 côté produit)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits_categorie", null=True, blank=True)
    statut = models.ForeignKey(Statut, on_delete=models.CASCADE, related_name="produits_status",null=True, blank=True)

    def __str__(self):
        return self.intituleProd

class Rayon(models.Model):
    idRayon = models.AutoField(primary_key=True)
    nomRayon = models.CharField(max_length=100)
    produits = models.ManyToManyField(
        'Produit',
        through='Contenir',
        related_name='rayon'
    )
    def __str__(self):
        return self.nomRayon

class Contenir(models.Model):
    produits = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="produits",null=False, blank=True)
    rayons = models.ForeignKey(Rayon, on_delete=models.CASCADE, related_name="rayons",null=False, blank=True)
    quantite = models.IntegerField(default=1)

    class Meta:
        unique_together = ('produits','rayons')

    def __str__(self):
        return f"Le rayon {self.rayons} contient ces produits {self.produits}"



    
