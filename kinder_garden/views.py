from django.shortcuts import render
from .models import Banner, SchoolClasses, PhotoGallery

def home(request):
    banners = Banner.objects.all()
    classes = SchoolClasses.objects.all()
    return render(request, 'index.html', {
        'banners': banners,
        'classes': classes
    })

def about(request):
    return render(request, 'about.html')    