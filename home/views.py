from django.shortcuts import render

# Create your views here.


from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import *



def home(request):
    return render(request, 'home/base.html',
                  {'home': home})

def about(request):
    return render(request, 'home/about.html',
                  {'about': about})


def mentor(request):
    return render(request, 'home/mentor.html',
                  {'mentor': mentor})