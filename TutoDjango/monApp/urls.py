from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
 path("home/", views.HomeView.as_view(), name ="home"),
 path("home/<param>", views.HomeView.as_view(),name="home"),
 path("aboutUs/", views.AboutView.as_view(),name="about"),
 path("contactUs/", views.ContactView,name="contact"),
 path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
 path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
 path("rayons/",views.RayonListView.as_view(),name="lst_rayons"),
 path("rayon/<pk>/" ,views.RayonDetailView.as_view(), name="dtl_rayon"),
 path("categories/",views.CategorieListView.as_view(),name="lst_categories"),
 path("categorie/<pk>/" ,views.CategorieDetailView.as_view(), name="dtl_categorie"),
 path("statuts/",views.StatutListView.as_view(),name="lst_statuts"),
 path("statut/<pk>/" ,views.StatutDetailView.as_view(), name="dtl_statut"),
 path("email-sent/",views.EmailSent,name="email-sent"),
 path('login/', views.ConnectView.as_view(), name='login'),
 path('register/', views.RegisterView.as_view(), name='register'),
 path('logout/', views.DisconnectView.as_view(), name='logout'),
]