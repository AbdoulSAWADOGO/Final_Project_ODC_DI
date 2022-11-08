from django.contrib import admin

# Register your models here.
from .models import citoyen,alerte #import the citoyen model

# Register your models here.
admin.site.register(citoyen)
admin.site.register(alerte)