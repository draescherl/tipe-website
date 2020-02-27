from django.shortcuts import render, get_object_or_404

from .models import Slide

# Create your views here.

def index(request):
    slides = Slide.objects.filter(display=True)
    context = {
        'slides' : slides
    }
    return render(request, 'presentation/slides.html', context)