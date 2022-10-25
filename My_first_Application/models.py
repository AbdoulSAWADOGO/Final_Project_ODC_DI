from django.db import models
from django.core.validators import MaxValueValidator ,MinValueValidator
# Create your models here.
from datetime import datetime, date
#Must inherit from Django Model class
class patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    nick_name = models.CharField(max_length=30)
    has_pet = models.BooleanField(default=True)
    number_pet = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def person_age(self):
        current_date = date.today()
        current_age = current_date.year-self.birth_date.year
        return f'{current_age}'
