from django.shortcuts import render
from .models import Destination

# Create your views here.

    # dest1 = Destination()
    # dest1.name = 'dest-1: Mumbai'
    # dest1.img = 'destination_1.jpg'
    # dest1.desc = 'desc: dest-1: mumbai: city'
    # dest1.price = '711'
    # dest1.offer = False


def index(request):
    dests = Destination.objects.all
    return render(request, 'index.html', {'dests': dests})
