from django.shortcuts import render
from django.http  import HttpResponse


from multiprocessing.spawn import is_forking
from django.shortcuts import render
from django.http import  HttpResponseRedirect,  HttpResponse
from My_first_Application.models import citoyen, alerte



def index(request):
    return render(request, 'Dossiers/index.html')

def onea(request):
    return render(request, 'Dossiers/ONEA.html')

def sonabel(request):
    return render(request, 'Dossiers/SONABEL.html')

def pompier(request):
    return render(request, 'Dossiers/pompier.html')

def autres(request):
    return render(request, 'Dossiers/autre.html')


def contact(request):
    return render(request, 'Dossiers/contact.html')

def connexion(request):
    return render(request, 'Dossiers/Connexion.html')

def apropos(request):
    return render(request, 'Dossiers/A_propos.html')
