from django.test import TestCase
from django.urls import reverse, resolve
from monApp.views import CategorieListView, CategorieDetailView,CategorieCreateView,CategorieUpdateView,CategorieDeleteView
from monApp.models import *
from django.contrib.auth.models import User

class CategorieCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_categorie_create_view_get(self):
        response = self.client.get(reverse('crt-categorie')) # Utilisation du nom de l'URL
        self.assertEqual(response.status_code, 200)
        # Tester que la vue de création renvoie le bon template
        self.assertTemplateUsed(response, 'monApp/create_categorie.html')

    def test_categorie_create_view_post_valid(self):
        data = { "nomCat": "CategoriePourTestCreation" }
        response = self.client.post(reverse('crt-categorie'), data)
        # Vérifie la redirection après la création
        self.assertEqual(response.status_code, 302)
        # Vérifie qu'un objet a été créé
        self.assertEqual(Categorie.objects.count(), 1)
        # Vérifie la valeur de l'objet créé
        self.assertEqual(Categorie.objects.last().nomCat, 'CategoriePourTestCreation')

class CategorieDetailViewTest(TestCase):

    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTestDetail")

    def test_categorie_detail_view(self):
        response = self.client.get(reverse('dtl_categorie', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_categorie.html')
        # Vérifie que le nom de la categorie est affiché
        self.assertContains(response, 'CategoriePourTestDetail')
        # Vérifie que l'id associé est affiché
        self.assertContains(response, '1')

class CategorieUpdateViewTest(TestCase):

    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTestUpdate")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_categorie_update_view_get(self):
        response = self.client.get(reverse('categorie-chng', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_categorie.html')

    def test_update_view_post_valid(self):
        self.assertEqual(self.ctgr.nomCat, 'CategoriePourTestUpdate')
        data = {'nomCat': 'CategoriePourTestAfterUpdate'}
        response = self.client.post(reverse('categorie-chng', args=[self.ctgr.idCat]), data)
        # Redirection après la mise à jour
        self.assertEqual(response.status_code, 302)
        # Recharger l'objet depuis la base de données
        self.ctgr.refresh_from_db()
        # Vérifier la mise à jour du nom
        self.assertEqual(self.ctgr.nomCat, 'CategoriePourTestAfterUpdate')

class CategorieDeleteViewTest(TestCase):

    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTesDelete")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_categorie_delete_view_get(self):
        response = self.client.get(reverse('dlt-categorie', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_categorie.html')

    def test_categorie_delete_view_post(self):
        response = self.client.post(reverse('dlt-categorie', args=[self.ctgr.idCat]))
        # Vérifier la redirection après la suppression
        self.assertEqual(response.status_code, 302)
        # Vérifier que l'objet a été supprimé
        self.assertFalse(Categorie.objects.filter(idCat=self.ctgr.idCat).exists())
        # Vérifier que la redirection est vers la liste des catégories
        self.assertRedirects(response, reverse('lst_categories'))