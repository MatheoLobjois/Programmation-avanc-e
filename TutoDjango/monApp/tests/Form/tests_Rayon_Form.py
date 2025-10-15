from django.test import TestCase
from monApp.forms import RayonForm
from monApp.models import Produit

class RayonFormTest(TestCase):
    def test_form_valid_data(self):
        produit = Produit.objects.create(intituleProd="ProduitTest", prixUnitaireProd=10, dateFabrication='2025-09-12' )
        form = RayonForm(data={'nomRayon': 'RayonPourTest', 'produits':{produit}})
        self.assertTrue(form.is_valid())
        rayon = form.save()
        self.assertEqual(rayon.nomRayon, 'RayonPourTest')
    
    def test_form_valid_data_too_long(self):
        form = RayonForm(data = {'nomRayon': 'RayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTestRayonPourTest'})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('nomRayon', form.errors) # Le champ 'nomRayon' doit contenir une erreur
        self.assertEqual(form.errors['nomRayon'], ['Assurez-vous que cette valeur comporte au plus 100 caractères (actuellement 234).'])
    
    def test_form_valid_data_missed(self):
        form = RayonForm(data = {'nomRayon': ''})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('nomRayon', form.errors) # Le champ 'nomRayon' doit contenir une erreur
        self.assertEqual(form.errors['nomRayon'], ['Ce champ est obligatoire.'])
    
    def test_form_save(self):
        produit = Produit.objects.create(intituleProd="ProduitTest", prixUnitaireProd=10, dateFabrication='2025-09-12' )
        form = RayonForm(data={'nomRayon': 'RayonPourTest', 'produits':{produit}})
        self.assertTrue(form.is_valid())
        rayon = form.save()
        self.assertEqual(rayon.nomRayon, 'RayonPourTest')
        self.assertEqual(rayon.idRayon, 1)