from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from monApp.views import ContenirCreateView, UpdateContenirView, DeleteContenirView
from monApp.models import Produit, Rayon, Contenir

class ContenirUrlsTest(TestCase):
    def setUp(self):
        # Création utilisateur connecté
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

        # Création de données de base
        self.rayon = Rayon.objects.create(nomRayon="RayonTest")
        self.produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=10,
            dateFabrication='2025-09-12'
        )

        # Création d’un objet Contenir
        self.contenir = Contenir.objects.create(
            produits=self.produit,
            rayons=self.rayon,
            quantite=5
        )
    #---------------------------Urls création contenir-------------------------------------------

    def test_contenir_create_url_is_resolved(self):
        url = reverse('cntnr-crt', args=[self.rayon.pk])
        self.assertEqual(resolve(url).view_name, 'cntnr-crt')
        self.assertEqual(resolve(url).func.view_class, ContenirCreateView)

    def test_contenir_create_response_code_OK(self):
        response = self.client.get(reverse('cntnr-crt', args=[self.rayon.pk]))
        self.assertEqual(response.status_code, 200)

    #---------------------------Urls update contenir-------------------------------------------

    def test_contenir_update_url_is_resolved(self):
        url = reverse('update_contenir', args=[self.rayon.pk, self.contenir.pk])
        self.assertEqual(resolve(url).view_name, 'update_contenir')
        self.assertEqual(resolve(url).func.view_class, UpdateContenirView)
    
    def test_contenir_update_response_code_OK(self):
        url = reverse('update_contenir', args=[self.rayon.pk, self.contenir.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contenir_update_response_code_KO(self):
        url = reverse('update_contenir', args=[self.rayon.pk, 9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    #---------------------------Urls delete contenir-------------------------------------------

    def test_contenir_delete_url_is_resolved(self):
        url = reverse('delete_contenir', args=[self.rayon.pk, self.contenir.pk])
        self.assertEqual(resolve(url).view_name, 'delete_contenir')
        self.assertEqual(resolve(url).func.view_class, DeleteContenirView)

    def test_contenir_delete_response_code_OK(self):
        url = reverse('delete_contenir', args=[self.rayon.pk, self.contenir.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contenir_delete_response_code_KO(self):
        url = reverse('delete_contenir', args=[self.rayon.pk, 9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    #--------------------------- Redirection après la création d'un objet contenir -------------------------------------------

    def test_redirect_after_contenir_creation(self):
        new_produit = Produit.objects.create(
            intituleProd="ProduitTest2",
            prixUnitaireProd=20,
            dateFabrication='2025-09-12'
        )
        response = self.client.post(
            reverse('cntnr-crt', args=[self.rayon.pk]),
            {'produits': new_produit.pk, 'quantite': 3}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dtl_rayon', args=[self.rayon.pk]))

    #---------------------------Redirection après la mise à jour d'un objet contenir -------------------------------------------

    def test_redirect_after_contenir_updating(self):
        response = self.client.post(
            reverse('update_contenir', args=[self.rayon.pk, self.contenir.pk]),
            data={'produits': self.produit.pk, 'quantite': 10}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dtl_rayon', args=[self.rayon.pk]))

    #---------------------------Redirection après la suppression d'un objet contenir -------------------------------------------
    
    def test_redirect_after_contenir_deletion(self):
        response = self.client.post(reverse('delete_contenir', args=[self.rayon.pk, self.contenir.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dtl_rayon', args=[self.rayon.pk]))
        self.assertFalse(Contenir.objects.filter(pk=self.contenir.pk).exists())
