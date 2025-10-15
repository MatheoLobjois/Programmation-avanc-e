from django.test import TestCase
from django.urls import reverse
from monApp.models import *
from django.contrib.auth.models import User

class RayonCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_rayon_create_view_get(self):
        response = self.client.get(reverse('crt-rayon')) # Utilisation du nom de l'URL
        self.assertEqual(response.status_code, 200)
        # Tester que la vue de création renvoie le bon template
        self.assertTemplateUsed(response, 'monApp/create_rayon.html')

    def test_rayon_create_view_post_valid(self):
        produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=10,
            dateFabrication='2025-09-12'
        )
        data = { 
            "nomRayon": "RayonPourTestCreation",
            "produits": [produit.refProd]  # ✅ ici on passe l'id, pas l'objet
        }
        response = self.client.post(reverse('crt-rayon'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Rayon.objects.count(), 1)
        self.assertEqual(Rayon.objects.last().nomRayon, 'RayonPourTestCreation')

class RayonDetailViewTest(TestCase):

    def setUp(self):
        self.ctgr = Rayon.objects.create(nomRayon="RayonPourTestDetail")

    def test_rayon_detail_view(self):
        response = self.client.get(reverse('dtl_rayon', args=[self.ctgr.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_rayon.html')
        # Vérifie que le nom de la rayon est affiché
        self.assertContains(response, 'RayonPourTestDetail')
        # Vérifie que l'id associé est affiché
        self.assertContains(response, '1')

class RayonUpdateViewTest(TestCase):

    def setUp(self):
        self.ctgr = Rayon.objects.create(nomRayon="RayonPourTestUpdate")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_rayon_update_view_get(self):
        response = self.client.get(reverse('rayon-chng', args=[self.ctgr.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_rayon.html')

    def test_update_view_post_valid(self):
        self.assertEqual(self.ctgr.nomRayon, 'RayonPourTestUpdate')
        produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=10,
            dateFabrication='2025-09-12'
        )
        data = { 
            "nomRayon": "RayonPourTestAfterUpdate",
            "produits": [produit.refProd]  # ✅ ici on passe l'id, pas l'objet
        }
        response = self.client.post(reverse('rayon-chng', args=[self.ctgr.idRayon]), data)
        # Redirection après la mise à jour
        self.assertEqual(response.status_code, 302)
        # Recharger l'objet depuis la base de données
        self.ctgr.refresh_from_db()
        # Vérifier la mise à jour du nom
        self.assertEqual(self.ctgr.nomRayon, 'RayonPourTestAfterUpdate')

class RayonDeleteViewTest(TestCase):

    def setUp(self):
        self.ctgr = Rayon.objects.create(nomRayon="RayonPourTesDelete")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_rayon_delete_view_get(self):
        response = self.client.get(reverse('dlt-rayon', args=[self.ctgr.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_rayon.html')

    def test_rayon_delete_view_post(self):
        response = self.client.post(reverse('dlt-rayon', args=[self.ctgr.idRayon]))
        # Vérifier la redirection après la suppression
        self.assertEqual(response.status_code, 302)
        # Vérifier que l'objet a été supprimé
        self.assertFalse(Rayon.objects.filter(idRayon=self.ctgr.idRayon).exists())
        # Vérifier que la redirection est vers la liste des catégories
        self.assertRedirects(response, reverse('lst_rayons'))