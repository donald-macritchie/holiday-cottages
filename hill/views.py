from django.shortcuts import render, get_object_or_404
from .models import Cottage, CottageImages, Amenities


def index(request):
    return render(request, "index.html")



def homestead_cottage(request):
    homestead_cottage = get_object_or_404(Cottage, name='Homestead')
    amenities = homestead_cottage.amenities.all()
    description = homestead_cottage.description

    content = {
        'homestead_cottage': homestead_cottage,
        'amenities': amenities,
        'description': description,
    }

    return render(request, 'homestead_cottage.html', content)


def marketview_cottage(request):
    marketview_cottage = get_object_or_404(Cottage, name='Homestead')
    amenities = marketview_cottage.amenities.all()
    description = marketview_cottage.description

    content = {
        'marketview_cottage': marketview_cottage,
        'amenities': amenities,
        'description': description,
    }

    return render(request, 'marketview_cottage.html', content)
