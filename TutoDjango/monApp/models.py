from django.db import models

class Categorie(models.Model):
    idCat = models.AutoField(primary_key=True)
    nomCat = models.CharField(max_length=100)

    def __str__(self):
        return self.nomCat
    
class Statut(models.Model):
    idStatut = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=200)
    
class Produit(models.Model):
    refProd = models.AutoField(primary_key=True)
    intituleProd = models.CharField(max_length=200)
    prixUnitaireProd = models.DecimalField(max_digits=10, decimal_places=2)
    dateFabrication = models.DateField(null=False, auto_now=True)
    # Relation CIF : chaque produit appartient à 1 catégorie (0,N côté catégorie 1,1 côté produit) →
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="produits",null=True, blank=True)
    statut = models.ForeignKey(Statut, on_delete=models.CASCADE, related_name="produits",null=True, blank=True)
    rayons = models.ManyToManyField(
        'Rayon',
        through='Contenir',
        related_name="produit"
    )
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

class Contenir(models.Model):
    produits = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name="produits",null=False, blank=True)
    rayons = models.ForeignKey(Rayon, on_delete=models.CASCADE, related_name="rayons",null=False, blank=True)
    pk = models.CompositePrimaryKey("produits", "rayons")
    quantite = models.IntegerField()



    
    