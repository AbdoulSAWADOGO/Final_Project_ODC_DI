from django.db import models
# from email.policy import default
# from random import choices
# from secrets import choice

# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date
from django.utils.translation import gettext_lazy as _
# Create your models here.
# from django.db.models import IntegerField, Model
# from django.core.validators import  MaxValueValidator, MinValueValidator 
#Must inherit from Django Model class

class UserCitoyen(AbstractUser):
    # GENRE = (("HOMME",'HOMME'),("FEMME","FEMME"))
    genre=models.CharField(_("genre"),max_length=20, null=True)
    telephone = models.CharField(_("telephone"),max_length=20, default="64896986")
    cnib = models.CharField(_("cnib"),max_length=50, default="B6541025410")
    def __str__(self):
        return self.username


class alerte(models.Model):
    type_de_probleme=models.CharField(max_length=50)
    niveau_du_probleme=models.CharField(max_length=100)
    commentaire_sur_le_probleme=models.CharField(max_length=400)
    structure=models.CharField(default="ONEA", max_length=20)
    profil = models.ImageField(upload_to='upload/',null=True,blank=True)
    def __str__(self):
        return self.structure






