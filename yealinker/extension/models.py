from django.db import models


# Create your models here.
class Extension(models.Model):
    number = models.CharField(name='Number', max_length=8)
    owner = models.CharField(name='Name', max_length=64)
    mac = models.CharField(name='MAC Address', max_length=32)
    group = models.ForeignKey(Group)
    email = models.EmailField(name='Email', max_length=64)

