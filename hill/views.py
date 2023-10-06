from django.shortcuts import render
from .models import Cottage, CottageImages, Amenities


def index(request):
    return render(request, "index.html")


def homestead_cottage(request):
    return render(request, 'homestead_cottage.html')
