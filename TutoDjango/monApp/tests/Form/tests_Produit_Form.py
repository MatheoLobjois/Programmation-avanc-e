from decimal import Decimal
from django.test import TestCase
from monApp.forms import ProduitForm

class ProduitFormTest(TestCase):
    def test_form_valid_data(self):
        form = ProduitForm(data = {'intituleProd': 'ProduitPourTest', 'prixUnitaireProd': '59.99', 'dateFabrication': '2025-09-09'})
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide
    
    def test_form_valid_data_too_long(self):
        form = ProduitForm(data = {'intituleProd': 'ProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTestProduitPourTest'})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors) # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Assurez-vous que cette valeur comporte au plus 200 caractères (actuellement 270).'])
    
    def test_form_valid_data_missed(self):
        form = ProduitForm(data = {'intituleProd': ''})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors) # Le champ 'intituleProd' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Ce champ est obligatoire.'])
    
    def test_form_save(self):
        form = ProduitForm(data = {'intituleProd': 'ProduitPourTest', 'prixUnitaireProd': '58.99', 'dateFabrication': '2025-09-09'})
        self.assertTrue(form.is_valid())
        produit = form.save()
        self.assertEqual(produit.intituleProd, 'ProduitPourTest')
        self.assertEqual(produit.prixUnitaireProd, Decimal('58.99'))
        self.assertEqual(produit.refProd, 1)