from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'dest-1: Mumbai'
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'desc: dest-1: mumbai: city'
    dest1.price = '711'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'dest-2: Mumbai'
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'desc: dest-2: mumbai: city'
    dest2.price = '722'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'dest-3: Mumbai'
    dest3.img = 'destination_4.jpg'
    dest3.desc = 'desc: dest-3: mumbai: city'
    dest3.price = '733'
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})
