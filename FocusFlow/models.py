from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Projet(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name='participes')

class Status(models.Model):
    nom = models.CharField(max_length=255)


class Tache(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='createdTasks')
    realizedBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='realizedTasks')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    projet = models.ManyToManyField(Projet, related_name='projetsTaches')


