# Generated by Django 5.1.3 on 2024-11-06 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher_django_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='UUID',
            new_name='id',
        ),
    ]
