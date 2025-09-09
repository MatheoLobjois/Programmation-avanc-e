from django.shortcuts import render

from django.http import HttpResponse
from .models import Produit, Categorie

def home(request ,param = "Django"):
    return HttpResponse(f"<h1>Hello {param} </h1>")


def about_us(request):
    return HttpResponse("<h1> About us </h1>")

def contact_us(request):
    return HttpResponse("<h1> ? </h1>")

def ListProduits(request):
    prdts = Produit.objects.all()
    liste = "<ul>"
    for produit in prdts:
        liste += f"""<li> {produit.intituleProd} </li>"""
    liste += "</ul>"
    return HttpResponse(liste)

def ListCategorie(request):
    cats = Categorie.objects.all()
    liste = "<ul>"
    for categorie in cats:
        liste += f"""<li> {categorie.nomCat} </li>"""
    liste += "</ul>"
    return HttpResponse(liste)

def ListStatut(request):
    prdts = Produit.objects.all()
    liste = "<ul>"
    for produit in prdts:
        liste += f"""<li> {produit.statut.libelle} </li>"""
    liste += "</ul>"
    return HttpResponse(liste)