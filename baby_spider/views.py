from django.shortcuts import render
from .models import Spider, Extract
from .forms import SpiderForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'baby_spider/home.html', {})


def list_spider(request):
    # if(request.POST.get('author') != None):
    author = request.POST.get('author')
    spiders = Spider.objects.filter(author=author)
    return render(request, 'baby_spider/spider_list.html', {'spiders':spiders})
    # else:
    #     return redirect('home')

def spider_new(request):
    if request.method == "POST":
        form = SpiderForm(request.POST)
        if form.is_valid():
            spider = form.save(commit=False)
            spider.save()
            return redirect('home')
    else:
        form = SpiderForm()
    return render(request, 'baby_spider/spider_edit.html', {'form': form})


def detail(request):
    return render(request, 'baby_spider/detail.html')
    

