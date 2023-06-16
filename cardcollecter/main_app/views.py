# main_app/views.py
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the Card Model
from .models import Card
from .forms import MarketForm

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


def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    market_form = MarketForm()
    return render(request, 'cards/detail.html', {
        'card' : card, 'market_form': market_form
    })

class CardCreate(CreateView):
    model = Card 
    fields = '__all__'

class CardUpdate(UpdateView):
    model = Card 
    fields = ['series', 'description', 'grade']

class CardDelete(DeleteView):
    model = Card 
    success_url = '/cards'

def add_market(request, card_id):
    form = MarketForm(request.POST)

    if form.is_valid():
        new_market = form.save(commit=False)
        new_market.card_id = card_id
        new_market.save()
    
    return redirect('detail', card_id=card_id)

