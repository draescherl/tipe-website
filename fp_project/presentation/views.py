from django.shortcuts import render

from .models import Slide

def index(request):
    slides = Slide.objects.filter(display=True)
    context = {
        'slides' : slides
    }
    return render(request, 'presentation/index.html', context)