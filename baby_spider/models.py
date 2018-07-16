from django.db import models
from django.utils import timezone

class Spider(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField()
    metodo = models.TextField()
    consulta = models.BooleanField(default=False)
    consulta_url = models.TextField(default=None)
    consulta_metodo = models.TextField(default=None)
    consulta_step2 = models.TextField(default=None)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    campo1 = models.TextField(default=None)
    campo2 = models.TextField(default=None)
    campo3 = models.TextField(default=None)
    campo4 = models.TextField(default=None)
    campo5 = models.TextField(default=None)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.author
