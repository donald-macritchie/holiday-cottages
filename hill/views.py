from django.shortcuts import render
from .models import Cottage, CottageImages, Amenities


def index(request):
    return render(request, "index.html")


def cottages(request):
    return render(request, "cottages.html")