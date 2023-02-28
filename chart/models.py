from django.db import models

# Create your models here.

class Visitor(models.Model):
    click = models.IntegerField()
    viewer = models.IntegerField()
