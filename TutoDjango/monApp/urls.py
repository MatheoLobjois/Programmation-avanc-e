from django.urls import path
from . import views

urlpatterns = [
 path("home/<param>", views.home, name="home_perso"),
 path("home/", views.home, name="home"),
 path("aboutUs/", views.about_us, name="about_us"),
 path("contactUs/", views.contact_us, name="contact_us"),
 path("listeProduits/",views.ListProduits, name="liste_produit"),
 path("listeCategorie/",views.ListCategorie, name="liste_categorie"),
 path("listeStatut/",views.ListStatut, name="liste_statut"),
]