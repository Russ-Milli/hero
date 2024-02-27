from django.shortcuts import render


def index(request):
    return render(request, 'html/index.html')


def about(request):
    return render(request, 'html/about.html')


def contact(request):
    return render(request, 'html/contact.html')


def products(request):
    return render(request, 'html/product.html')


def remote(request):
    return render(request, 'html/remot.html')


def videos(request):
    return render(request, 'html/video.html')

# Create your views here.
