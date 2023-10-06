from django.shortcuts import render, get_object_or_404
from .models import Cottage, CottageImages, Amenities


def index(request):
    return render(request, "index.html")


# def homestead_cottage(request):
#     amenities = homestead_cottage.amenities.all()
#     return render(request, 'homestead_cottage.html')


def homestead_cottage(request):
    homestead_cottage = get_object_or_404(Cottage, name='Homestead')

    amenities = homestead_cottage.amenities.all()

    context = {
        'homestead_cottage': homestead_cottage,
        'amenities': amenities,
    }

    return render(request, 'homestead_cottage.html', context)
