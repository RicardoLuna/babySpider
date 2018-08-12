from django.db import models
from django.utils import timezone

class Spider(models.Model):
    url = models.CharField(max_length=200, default = '')
    author = models.CharField(max_length=150, default = '')
    campo1 = models.CharField(max_length=150, default = '')
    campo2 = models.CharField(max_length=150, default = '')
    campo3 = models.CharField(max_length=150, default = '')
    campo4 = models.CharField(max_length=150, default = '')
    campo5 = models.CharField(max_length=150, default = '')

    def __str__(self):
        return self.author

class Extract(models.Model):
    
    author = models.TextField(default='vazio')
    fonte =  models.TextField(default='vazio')
    campo1 = models.TextField(default='vazio')
    campo2 = models.TextField(default='vazio')
    campo3 = models.TextField(default='vazio')
    campo4 = models.TextField(default='vazio')
    campo5 = models.TextField(default='vazio')

    def __str__(self):
        return self.author
