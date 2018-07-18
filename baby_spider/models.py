from django.db import models
from django.utils import timezone

class Spider(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100)
    metodo = models.CharField(max_length=200)
    consulta = models.BooleanField(default=False)
    consulta_url = models.CharField(max_length=100)
    consulta_metodo = models.CharField(max_length=50)
    consulta_step2 = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    campo1 = models.CharField(max_length=50)
    campo2 = models.CharField(max_length=50)
    campo3 = models.CharField(max_length=50)
    campo4 = models.CharField(max_length=50)
    campo5 = models.CharField(max_length=50)

    def __str__(self):
        return self.author


class Extract(models.Model):
    
    id = models.AutoField(primary_key=True)
    author = models.TextField(default=None)
    campo2 = models.TextField(default=None)
    campo3 = models.TextField(default=None)
    campo4 = models.TextField(default=None)
    campo5 = models.TextField(default=None)

    def __str__(self):
        return self.author
