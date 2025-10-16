from django.test import TestCase
from django.urls import reverse
from monApp.models import Produit, Rayon, Contenir
from django.contrib.auth.models import User

class ContenirCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.rayon = Rayon.objects.create(nomRayon="RayonTest")

    def test_contenir_create_view_get(self):
        response = self.client.get(reverse('cntnr-crt', args=[self.rayon.idRayon]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/create_contenir.html')

    def test_contenir_create_view_post_valid(self):
        produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=10,
            dateFabrication='2025-09-12'
        )
        data = { 
            "produits": produit.refProd,
            "quantite": 3
        }
        response = self.client.post(reverse('cntnr-crt', args=[self.rayon.idRayon]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Contenir.objects.count(), 1)
        contenir = Contenir.objects.last()
        self.assertEqual(contenir.produits, produit)
        self.assertEqual(contenir.rayons, self.rayon)
        self.assertEqual(contenir.quantite, 3)


class ContenirUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.rayon = Rayon.objects.create(nomRayon="RayonTest")
        self.produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=10,
            dateFabrication='2025-09-12'
        )
        self.contenir = Contenir.objects.create(
            rayons=self.rayon,
            produits=self.produit,
            quantite=1
        )

    def test_contenir_update_view_get(self):
        response = self.client.get(reverse('update_contenir', args=[self.rayon.idRayon, self.contenir.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_contenir.html')

    def test_contenir_update_view_post_valid(self):
        data = { 
            "produits": self.produit.refProd,
            "quantite": 10
        }
        response = self.client.post(reverse('update_contenir', args=[self.rayon.idRayon, self.contenir.id]), data)
        self.assertEqual(response.status_code, 302)
        self.contenir.refresh_from_db()
        self.assertEqual(self.contenir.quantite, 10)


class ContenirDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.rayon = Rayon.objects.create(nomRayon="RayonTest")
        self.produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=10,
            dateFabrication='2025-09-12'
        )
        self.contenir = Contenir.objects.create(
            rayons=self.rayon,
            produits=self.produit,
            quantite=1
        )

    def test_contenir_delete_view_get(self):
        response = self.client.get(reverse('delete_contenir', args=[self.rayon.idRayon, self.contenir.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_contenir.html')

    def test_contenir_delete_view_post(self):
        response = self.client.post(reverse('delete_contenir', args=[self.rayon.idRayon, self.contenir.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Contenir.objects.filter(id=self.contenir.id).exists())
        self.assertRedirects(response, reverse('dtl_rayon', args=[self.rayon.idRayon]))
