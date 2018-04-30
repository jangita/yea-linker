from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(name='Name', max_length=64)

