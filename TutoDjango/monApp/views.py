from django.shortcuts import render

from django.http import HttpResponse, Http404
from .models import Produit, Categorie,Statut,Rayon

def home(request):
    if request.GET and request.GET["name"]:
        raise Http404
    return HttpResponse("Bonjour Monde!")


def about_us(request):
    return render(request, 'monApp/about_us.html')
def contact_us(request):
    return render(request, 'monApp/contact_us.html')

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html',{'prdts': prdts})

def ListCategorie(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html',{'cats': cats})

def ListStatut(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html',{'stats': stats})

def ListRayon(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html',{'rayons': rayons})