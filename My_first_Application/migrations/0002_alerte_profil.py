# Generated by Django 4.1.1 on 2022-11-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_first_Application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerte',
            name='profil',
            field=models.ImageField(blank=True, null=True, upload_to='profil'),
        ),
    ]