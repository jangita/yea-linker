from django.db import models
from extension.models import Extension


# Create your models here.
class SpeedDial(models.Model):
    caller = models.ForeignKey(Extension, name='Owner')
    callee = models.ForeignKey(Extension, name='Extension')
    position = models.IntegerField(name='Position')
