# Generated by Django 5.1.3 on 2025-01-03 11:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FocusFlow', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='user',
        ),
        migrations.AddField(
            model_name='tache',
            name='user',
            field=models.ManyToManyField(related_name='participes', to=settings.AUTH_USER_MODEL),
        ),
    ]
