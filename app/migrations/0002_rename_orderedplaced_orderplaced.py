# Generated by Django 4.0.6 on 2022-07-20 11:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderedPlaced',
            new_name='OrderPlaced',
        ),
    ]
