import requests
import re

from django.shortcuts import render
from .models import Spider, Extract
from .forms import SpiderForm
from django.shortcuts import redirect
from lxml import html

def home(request):
    return render(request, 'baby_spider/home.html', {})


def list_spider(request):
    author = request.POST.get('author')
    spiders = Spider.objects.filter(author=author)
    return render(request, 'baby_spider/spider_list.html', {'spiders': spiders})

def list_extract(request):
    author = request.POST.get('author')
    extracts = Extract.objects.filter(author=author)
    return render(request, 'baby_spider/extract_list.html', {'extracts': extracts})


def spider_new(request):
    if request.method == "POST":
        form = SpiderForm(request.POST)
        if form.is_valid():
            spider = form.save(commit=False)
            spider.save()
            extract(form)
            return redirect('home')
    else:
        form = SpiderForm()
    return render(request, 'baby_spider/spider_edit.html', {'form': form})


def detail(request):
    return render(request, 'baby_spider/detail.html')

def extract(form):
    author = form['author'].value()
    fonte = form['url'].value()
    campo1 = form['campo1'].value()
    campo2 = form['campo2'].value()
    campo3 = form['campo3'].value()
    campo4 = form['campo4'].value()
    campo5 = form['campo5'].value()

    page_query = requests.get(fonte)
    tree = html.fromstring(page_query.content)
    
    result_campo1 = re.sub('\s+', '',''.join(tree.xpath(campo1)))
    result_campo2 = re.sub('\s+', '',''.join(tree.xpath(campo2)))
    result_campo3 = re.sub('\s+', '',''.join(tree.xpath(campo3)))
    result_campo4 = re.sub('\s+', '',''.join(tree.xpath(campo4)))
    result_campo5 = re.sub('\s+', '',''.join(tree.xpath(campo5)))


    extract = Extract(author = author, fonte = fonte, campo1 = result_campo1, campo2 = result_campo2, campo3 = result_campo3, campo4 =result_campo4, campo5 = result_campo5)
    extract.save()

    
    

