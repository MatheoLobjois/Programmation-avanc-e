from django.test import TestCase
from monApp.models import Contenir, Rayon, Produit

class ContenirModelTest(TestCase):
    def setUp(self):
        self.produit = Produit.objects.create(intituleProd="prod", prixUnitaireProd=59.99, dateFabrication='2025-09-09')
        self.rayon = Rayon.objects.create(nomRayon="rayon")
        self.contenir = Contenir.objects.create(produits=self.produit, rayons=self.rayon, quantite=60)

    def test_contenir_create(self):
        self.assertEqual(self.contenir.quantite, 60)
        self.assertEqual(self.contenir.produits, self.produit)
        self.assertEqual(self.contenir.rayons, self.rayon)

    def test_string_repr(self):
        self.assertEqual(str(self.contenir), f"Le rayon {self.contenir.rayons.nomRayon} contient ces produits {self.contenir.produits.intituleProd}")

    def test_contenir_update(self):
        self.contenir.quantite = 50
        self.contenir.save()

        update_contenir = Contenir.objects.get(id=self.contenir.id)
        self.assertEqual(update_contenir.quantite, 50)

    def test_contenir_delete(self):
        self.contenir.delete()
        self.assertEqual(Contenir.objects.count(), 0)