from django.shortcuts import render

from .models import Slide
from .forms import SignUpForm


def index(request):
    slides = Slide.objects.filter(display=True)
    context = {
        'slides' : slides
    }
    return render(request, 'presentation/index.html', context)


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
