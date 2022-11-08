from django.shortcuts import render
from django.http  import HttpResponse

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login 
# from multiprocessing.spawn import is_forking
# from django.shortcuts import render
# from django.http import  HttpResponseRedirect,  HttpResponse
from My_first_Application.models import citoyen, alerte



def index(request):
    return render(request, 'Dossiers/index.html')

def onea(request):
    error = {}
    message = ''
    if request.method == "POST":
        if 'type_alerte' not in request.POST:
            error['type_alerte'] = "type d'alerte non founit"
        if 'niveau_problème' not in request.POST:
            error['niveau_problème'] = "niveau de problème non founit"
        if 'commentaire' not in request.POST:
            error['commentaire'] = "commentaire non founit"
        print(error)
        if len(error) == 0:
            alerte.objects.create(
                structure = "ONEA",
                type_de_probleme = request.POST['type_alerte'],
                niveau_du_probleme = request.POST['niveau_problème'],
                commentaire_sur_le_probleme = request.POST['commentaire']
            )
            message = "Alerte créée avec succès"
        else :
            message = "Une erreur s'est produite"
    context = {
        'message' : message,
    }
    return render(request, 'Dossiers/ONEA.html', context)

def sonabel(request):
    error = {}
    message = ''
    if request.method == "POST":
        if 'type_alerte' not in request.POST:
            error['type_alerte'] = "type d'alerte non founit"
        if 'niveau_problème' not in request.POST:
            error['niveau_problème'] = "niveau de problème non founit"
        if 'commentaire' not in request.POST:
            error['commentaire'] = "commentaire non founit"
        print(error)
        if len(error) == 0:
            alerte.objects.create(
                structure = "SONABEL",
                type_de_probleme = request.POST['type_alerte'],
                niveau_du_probleme = request.POST['niveau_problème'],
                commentaire_sur_le_probleme = request.POST['commentaire']
            )
            message = "Alerte créée avec succès"
        else :
            message = "Une erreur s'est produite"
    context = {
        'message' : message,
    }
    return render(request, 'Dossiers/SONABEL.html', context)

def pompier(request):
    error = {}
    message = ''
    if request.method == "POST":
        if 'type_alerte' not in request.POST:
            error['type_alerte'] = "type d'alerte non founit"
        if 'niveau_problème' not in request.POST:
            error['niveau_problème'] = "niveau de problème non founit"
        if 'commentaire' not in request.POST:
            error['commentaire'] = "commentaire non founit"
        print(error)
        if len(error) == 0:
            alerte.objects.create(
                structure = "POMPIERS",
                type_de_probleme = request.POST['type_alerte'],
                niveau_du_probleme = request.POST['niveau_problème'],
                commentaire_sur_le_probleme = request.POST['commentaire']
            )
            message = "Alerte créée avec succès"
        else :
            message = "Une erreur s'est produite"
    context = {
        'message' : message,
    }
    return render(request, 'Dossiers/pompier.html', context)

def autres(request):
    error = {}
    message = ''
    if request.method == "POST":
        if 'type_alerte' not in request.POST:
            error['type_alerte'] = "type d'alerte non founit"
        if 'niveau_problème' not in request.POST:
            error['niveau_problème'] = "niveau de problème non founit"
        if 'commentaire' not in request.POST:
            error['commentaire'] = "commentaire non founit"
        print(error)
        if len(error) == 0:
            alerte.objects.create(
                structure = "AUTRES",
                type_de_probleme = request.POST['type_alerte'],
                niveau_du_probleme = request.POST['niveau_problème'],
                commentaire_sur_le_probleme = request.POST['commentaire']
            )
            message = "Alerte créée avec succès"
        else :
            message = "Une erreur s'est produite"
    context = {
        'message' : message,
    }
    return render(request, 'Dossiers/autre.html', context)


def contact(request):
    return render(request, 'Dossiers/contact.html')

def connexion(request):
    
    error={}
    print("connexion")
    if request.method == "POST":
        print("post..............")
        if "username" not in request.POST:
            error["username"]="username non remplit"
        if "password" not in request.POST:
            error["password"]="mot de passe non remplit"
        if len(error)==0:
            user= authenticate(request, username=request.POST["username"], password=request.POST["password"])
            print("user................")
            print(user)
            if user is not None:
                login(request, user)
                print("Utilisateur connecté")
                return redirect('index')
            print("utilisateur non trouvé")
    return render(request, 'Dossiers/Connexion.html')

def apropos(request):
    return render(request, 'Dossiers/A_propos.html')
