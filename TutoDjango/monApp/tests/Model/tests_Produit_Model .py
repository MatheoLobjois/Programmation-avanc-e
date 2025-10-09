from django.test import TestCase
from monApp.models import *

class ProduitModelTest(TestCase):
    def setUp(self):
        
        self.prdt = Produit.objects.create(intituleProd="ProdPourTest")

    def test_categorie_creation(self):
        self.assertEqual(self.prdt.intituleProd, "ProdPourTest")

    def test_string_representation(self):
        self.assertEqual(str(self.prdt), "ProdPourTest")
    
    def test_categorie_updating(self):
        self.prdt.intituleProd = "ProdPourTest"
        self.prdt.save()
        # Récupérer l'objet mis à jour
        updated_prdt = Produit.objects.get(refProd=self.prdt.refProd)
        self.assertEqual(updated_prdt.intituleProd, "ProdPourTest")
    
    def test_categorie_deletion(self):
        self.prdt.delete()
        self.assertEqual(Produit.objects.count(), 0)