from django.test import TestCase
from monApp.forms import *
class ProduitFormTest(TestCase):

    def test_form_valid_data(self):
        form = ProduitForm(data = {'intituleProd': 'ProduitPourTest'})
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide
    
    def test_form_valid_data_too_long(self):
        form = ProduitForm(data = {'intituleProd': 'CategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTestCategoriePourTest'})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors) # Le champ 'nomCat' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Assurez-vous que cette valeur comporte au plus 200 caractères (actuellement 306).'])
    
    def test_form_valid_data_missed(self):
        form = ProduitForm(data = {'intituleProd': ''})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('intituleProd', form.errors) # Le champ 'nomCat' doit contenir une erreur
        self.assertEqual(form.errors['intituleProd'], ['Ce champ est obligatoire.'])
    
    def test_form_save(self):
        form = ProduitForm(data = {'intituleProd': 'ProduitPourTest'})
        self.assertTrue(form.is_valid())
        prdt = form.save()
        self.assertEqual(prdt.intituleProd, 'ProduitPourTest')
        self.assertEqual(prdt.refProd, 1)