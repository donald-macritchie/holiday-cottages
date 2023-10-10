from django.shortcuts import render, get_object_or_404
from .models import Cottage, CottageImages, Amenities, ThingsToKnow
import os


def index(request):
    return render(request, "index.html")


def homestead_cottage(request):
    homestead_cottage = get_object_or_404(Cottage, name='Homestead')
    amenities = homestead_cottage.amenities.all()
    description = homestead_cottage.description
    things_to_know = homestead_cottage.things_to_know.all()

    content = {
        'homestead_cottage': homestead_cottage,
        'amenities': amenities,
        'description': description,
        'GOOGLEMAPS_API_KEY': os.environ.get('GOOGLEMAPS_API_KEY', ''),
        'things_to_know': things_to_know,
    }

    return render(request, 'homestead_cottage.html', content)


def marketview_cottage(request):
    marketview_cottage = get_object_or_404(Cottage, name='Marketview')
    amenities = marketview_cottage.amenities.all()
    description = marketview_cottage.description,
    

    things_to_know_by_category = {}
    things_to_know = marketview_cottage.things_to_know.all()

    for category, _ in ThingsToKnow.CATEGORY_CHOICES:
        things_to_know_by_category[category] = things_to_know.filter(
            category=category)

    content = {
        'marketview_cottage': marketview_cottage,
        'amenities': amenities,
        'description': description,
        'GOOGLEMAPS_API_KEY': os.environ.get('GOOGLEMAPS_API_KEY', ''),
        'things_to_know_by_category': things_to_know_by_category,
    }

    return render(request, 'marketview_cottage.html', content)
