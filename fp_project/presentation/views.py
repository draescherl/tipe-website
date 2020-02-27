from django.shortcuts import render, get_object_or_404
# from django.db import transaction

from .models import Slide

# Create your views here.

# @transaction.atomic
def slide(request, slide_id):
    slide = get_object_or_404(Slide, pk=slide_id)
    context = {
        'slide_name' : slide.name,
        'slide_title' : slide.title,
        'slide_content' : slide.content,
    }
    return render(request, 'presentation/slide_base.html', context)