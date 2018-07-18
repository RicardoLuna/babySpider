from django.shortcuts import render
from .models import Spider, Extract
from .forms import SpiderForm

# Create your views here.
def spider_list(request):
    return render(request, 'baby_spider/spider_list.html', {})


def extract_list(request, name):
    posts = Post.objects.filter(author=name)
    return render(request, 'baby_spider/spider_list.html', {})


def spider_new(request):
    if request.method == "POST":
        form = SpiderForm(request.POST)
        if form.is_valid():
            spider = form.save(commit=False)
            spider.save()
            return redirect('base', pk=post.pk)
    else:
        form = SpiderForm()
    return render(request, 'baby_spider/spider_edit.html', {'form': form})