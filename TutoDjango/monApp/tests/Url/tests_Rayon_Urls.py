from django.test import TestCase
from django.urls import reverse, resolve
from monApp.views import RayonListView, RayonDetailView,RayonCreateView,RayonUpdateView,RayonDeleteView
from monApp.models import *
from django.contrib.auth.models import User

class RayonUrlsTest(TestCase):
    def setUp(self):
        self.rayon = Rayon.objects.create(nomRayon="RayonPourTest")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_rayon_detail_response_code(self):
        url = reverse('dtl_rayon', args=[self.rayon.idRayon]) #idCat existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_rayon_create_response_code_OK(self):
        response = self.client.get(reverse('crt-rayon'))
        self.assertEqual(response.status_code, 200)

    def test_rayon_detail_response_code_KO(self):
        url = reverse('dtl_rayon', args=[9999]) # idCat non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_rayon_list_url_is_resolved(self):
        url = reverse('lst_rayons')
        self.assertEqual(resolve(url).view_name, 'lst_rayons')
        self.assertEqual(resolve(url).func.view_class,RayonListView)

    def test_rayon_detail_url_is_resolved(self):
        url = reverse('dtl_rayon', args=[1])
        self.assertEqual(resolve(url).view_name, 'dtl_rayon')
        self.assertEqual(resolve(url).func.view_class, RayonDetailView)

    def test_rayon_create_url_is_resolved(self):
        url = reverse('crt-rayon')
        self.assertEqual(resolve(url).view_name, 'crt-rayon')
        self.assertEqual(resolve(url).func.view_class, RayonCreateView)

    def test_rayon_update_url_is_resolved(self):
        url = reverse('rayon-chng', args=[1])
        self.assertEqual(resolve(url).view_name, 'rayon-chng')
        self.assertEqual(resolve(url).func.view_class, RayonUpdateView)

    def test_rayon_delete_url_is_resolved(self):
        url = reverse('dlt-rayon', args=[1])
        self.assertEqual(resolve(url).view_name, 'dlt-rayon')
        self.assertEqual(resolve(url).func.view_class, RayonDeleteView)
    
    def test_rayon_list_response_code(self):
        response = self.client.get(reverse('lst_rayons'))
        self.assertEqual(response.status_code, 200)
    
    def test_rayon_update_response_code_OK(self):
        url = reverse('rayon-chng', args=[self.rayon.idRayon]) # idCat existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_rayon_update_response_code_KO(self):
        url = reverse('rayon-chng', args=[9999]) # idCat non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_rayon_delete_response_code_OK(self):
        url = reverse('dlt-rayon', args=[self.rayon.idRayon]) # idCat existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_rayon_delete_response_code_KO(self):
        url = reverse('dlt-rayon', args=[9999]) # idCat non existant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_redirect_after_rayon_creation(self):
        produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=10,
            dateFabrication='2025-09-12'
        )
        response = self.client.post(reverse('crt-rayon'), {'nomRayon': 'RayonPourTestRedirectionCreation',"produits": [produit.refProd]})
        # Statut 302 = redirection
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail
        self.assertRedirects(response, '/monApp/rayon/2/')

    def test_redirect_after_rayon_updating(self):
        produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=10,
            dateFabrication='2025-09-12'
        )
        response = self.client.post(reverse('rayon-chng', args=[self.rayon.idRayon]),
        data={"nomRayon": "RayonPourTestRedirectionMaj","produits": [produit.refProd]})
        # Statut 302 = redirection
        self.assertEqual(response.status_code, 302)
        # Redirection vers la vue de detail
        self.assertRedirects(response, f'/monApp/rayon/{self.rayon.idRayon}/')

    def test_redirect_after_rayon_deletion(self):
        response = self.client.post(reverse('dlt-rayon', args=[self.rayon.pk]))
        # Vérifie qu'on a bien une redirection
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lst_rayons'))
        # Vérifie que la catégorie a bien été supprimée de la base
        self.assertFalse(Rayon.objects.filter(pk=self.rayon.pk).exists())