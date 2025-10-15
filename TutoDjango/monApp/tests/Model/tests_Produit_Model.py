from django.test import TestCase
from monApp.models import Produit

class ProduitModelTest(TestCase):
    def setUp(self):
        self.produit = Produit.objects.create(intituleProd="ProduitPourTest", prixUnitaireProd=59.99, dateFabrication="2025-09-09")

    def test_produit_create(self):
        self.assertEqual(self.produit.intituleProd, "ProduitPourTest")

    def test_string_repr(self):
        self.assertEqual(str(self.produit), "ProduitPourTest")

    def test_produit_update(self):
        self.produit.intituleProd = "ProduitPourTests"
        self.produit.save()

        update_produit = Produit.objects.get(refProd=self.produit.refProd)
        self.assertEqual(update_produit.intituleProd, "ProduitPourTests")

    def test_produit_delete(self):
        self.produit.delete()
        self.assertEqual(Produit.objects.count(), 0)
