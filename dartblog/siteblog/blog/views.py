from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def get_category(request, slug):
    return render(request, 'blog/category.html')