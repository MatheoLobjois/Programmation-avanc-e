from django.shortcuts import render

from django.http import HttpResponse

def home(request ,param = "Django"):
    return HttpResponse(f"<h1>Hello {param} </h1>")


def about_us(request):
    return HttpResponse("<h1> About us </h1>")

def contact_us(request):
    return HttpResponse("<h1> ? </h1>")