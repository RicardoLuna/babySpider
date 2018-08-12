from django.contrib import admin
from .models import Spider, Extract

admin.site.register([Spider, Extract])
