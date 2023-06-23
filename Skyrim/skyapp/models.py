from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class PocionWiki(models.Model):
    nombre = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=2000)
    def __str__(self) -> str:
        return f'Pocion: {self.nombre} {self.ingredientes}'
    
