from django.db import models
# from email.policy import default
# from random import choices
# from secrets import choice

# Create your models here.

from datetime import datetime, date
# Create your models here.
# from django.db.models import IntegerField, Model
# from django.core.validators import  MaxValueValidator, MinValueValidator 
#Must inherit from Django Model class
class citoyen(models.Model):
    GENRE = (("HOMME",'HOMME'),("FEMME","FEMME"))
    genre=models.CharField(max_length=20,choices=GENRE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    email=models.CharField(max_length=50, default="admin@default.com")
    telephone=models.CharField(max_length=10)
    cnib=models.CharField(max_length=50, default="B6541025410")

    def __str__(self):
        return self.last_name


class alerte(models.Model):
    type_de_probleme=models.CharField(max_length=50)
    niveau_du_probleme=models.CharField(max_length=100)
    commentaire_sur_le_probleme=models.CharField(max_length=400)
    structure=models.CharField(default="ONEA", max_length=20)
    def __str__(self):
        return self.structure






