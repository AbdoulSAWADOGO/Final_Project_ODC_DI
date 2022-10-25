from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('Dossiers/ONEA.html', views.onea, name='onea'),
    path('Dossiers/SONABEL.html', views.sonabel, name='sonabel'),
    path('Dossiers/pompier.html', views.pompier, name='pompiers'),
    path('Dossiers/autre.html', views.autres, name='autres'),
    path('Dossiers/contact.html', views.contact, name='contact'),
    path('Dossiers/Connexion.html', views.connexion, name='connexion'),
    path('Dossiers/A_propos.html', views.apropos, name='apropos'),

]
