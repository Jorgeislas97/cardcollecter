# main_app/views.py
from django.shortcuts import render
# Import the Cat Model
from .models import Card


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {
    'cards': cards
  })
