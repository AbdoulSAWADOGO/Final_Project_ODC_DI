from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('Dossiers/ONEA', views.onea, name='onea'),
    path('Dossiers/SONABEL', views.sonabel, name='sonabel'),
    path('Dossiers/pompier', views.pompier, name='pompiers'),
    path('Dossiers/autre', views.autres, name='autres'),
    path('Dossiers/contact', views.contact, name='contact'),
    path('Dossiers/Connexion', views.connexion, name='connexion'),
    path('Dossiers/A_propos', views.apropos, name='apropos'),

]
