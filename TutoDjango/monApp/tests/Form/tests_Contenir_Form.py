from django.test import TestCase
from monApp.forms import ContenirForm
from monApp.models import Produit, Rayon

class ContenirFormTest(TestCase):
    def test_form_valid_data(self):
        produit = Produit.objects.create(intituleProd="prod", prixUnitaireProd=59.99, dateFabrication='2025-09-09')
        form = ContenirForm(data = {'produits': produit, 'quantite': 60})
        self.assertTrue(form.is_valid()) # Le formulaire doit être valide

    def test_form_valid_data_missed(self):
        form = ContenirForm(data = {'quantite': 60})
        self.assertFalse(form.is_valid()) # Le formulaire doit être invalide
        self.assertIn('produits', form.errors) # Le champ 'nomContenir' doit contenir une erreur
        self.assertEqual(form.errors['produits'], ['Ce champ est obligatoire.'])
    
    def test_form_save(self):
        produit = Produit.objects.create(intituleProd="prod", prixUnitaireProd=59.99, dateFabrication='2025-09-09')
        rayon = Rayon.objects.create(nomRayon="RayonPourTest")
        form = ContenirForm(data = {'produits': produit, 'quantite': 60})
        self.assertTrue(form.is_valid())
        contenir = form.save(commit=False)
        contenir.rayons = rayon
        contenir.save()
        self.assertEqual(contenir.quantite, 60)
        self.assertEqual(contenir.id, 1)