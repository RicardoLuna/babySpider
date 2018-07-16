from django.shortcuts import render

# Create your views here.
def spider_list(request):
    return render(request, 'baby_spider/spider_list.html', {})