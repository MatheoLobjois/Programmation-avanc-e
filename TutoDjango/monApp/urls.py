from django.urls import path
from . import views

urlpatterns = [
 path("home/<param>", views.home, name="home_perso"),
 path("home/", views.home, name="home"),
 path("AboutUs", views.about_us, name="about_us"),
 path("ContactUs", views.contact_us, name="contact_us"),
]