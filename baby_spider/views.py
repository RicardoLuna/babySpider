from django.shortcuts import render
from .models import Spider, Extract

# Create your views here.
def spider_list(request):
    return render(request, 'baby_spider/spider_list.html', {})


def extract_list(request, name):
    posts = Post.objects.filter(author=name)
    return render(request, 'baby_spider/spider_list.html', {})