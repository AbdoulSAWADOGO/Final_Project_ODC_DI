from django.contrib import admin

# Register your models here.
from .models import alerte, UserCitoyen #import the citoyen model

# Register your models here.
admin.site.register(alerte)
admin.site.register(UserCitoyen)