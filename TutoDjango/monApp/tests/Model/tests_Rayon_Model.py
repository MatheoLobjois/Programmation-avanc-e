from django.test import TestCase
from monApp.models import *

class RayonModelTest(TestCase):
    def setUp(self):
        
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTest")

    def test_categorie_creation(self):
        self.assertEqual(self.rayon.nomRayon, "RayonPourTest")

    def test_string_representation(self):
        self.assertEqual(str(self.rayon), "RayonPourTest")
    
    def test_categorie_updating(self):
        self.rayon.nomRayon = "RayonPourTest"
        self.rayon.save()
        # Récupérer l'objet mis à jour
        updated_rayon = Rayon.objects.get(nomRayon=self.rayon.nomRayon)
        self.assertEqual(updated_rayon.nomRayon, "RayonPourTest")
    
    def test_categorie_deletion(self):
        self.rayon.delete()
        self.assertEqual(Rayon.objects.count(), 0)