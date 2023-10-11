from django.shortcuts import render, get_object_or_404
from .models import Cottage, CottageImages, Amenities, ThingsToKnow
from .forms import BookingForm
import os

#  Home Page
def index(request):
    return render(request, "index.html")


# Homestead Cottage
def homestead_cottage(request):
    homestead_cottage = get_object_or_404(Cottage, name='Homestead')
    description = homestead_cottage.description

    # Amenities
    amenities = homestead_cottage.amenities.all()
    amenities_by_category = {}

    for category, _ in Amenities.CATEGORY_CHOICES:
        amenities_by_category[category] = amenities.filter(category=category)

    # Things to Know
    things_to_know_by_category = {}
    things_to_know = homestead_cottage.things_to_know.all()

    for category, _ in ThingsToKnow.CATEGORY_CHOICES:
        things_to_know_by_category[category] = things_to_know.filter(
            category=category)

    no_of_bedrooms = homestead_cottage.no_of_bedrooms
    no_of_bathrooms = homestead_cottage.no_of_bathrooms

    # BookingForm
    booking_form = BookingForm()

    content = {
        'homestead_cottage': homestead_cottage,
        'amenities_by_category': amenities_by_category,
        'description': description,
        'GOOGLEMAPS_API_KEY': os.environ.get('GOOGLEMAPS_API_KEY', ''),
        'things_to_know_by_category': things_to_know_by_category,
        'no_of_bedrooms': no_of_bedrooms,
        'no_of_bathrooms': no_of_bathrooms,
        'booking_form': booking_form,
    }

    return render(request, 'homestead_cottage.html', content)


# Marketview Cottage
def marketview_cottage(request):
    marketview_cottage = get_object_or_404(Cottage, name='Marketview')
    description = marketview_cottage.description

    amenities = marketview_cottage.amenities.all()
    amenities_by_category = {}

    for category, _ in Amenities.CATEGORY_CHOICES:
        amenities_by_category[category] = amenities.filter(category=category)

    things_to_know_by_category = {}
    things_to_know = marketview_cottage.things_to_know.all()

    for category, _ in ThingsToKnow.CATEGORY_CHOICES:
        things_to_know_by_category[category] = things_to_know.filter(
            category=category)

    no_of_bedrooms = marketview_cottage.no_of_bedrooms
    no_of_bathrooms = marketview_cottage.no_of_bathrooms

    content = {
        'marketview_cottage': marketview_cottage,
        'amenities_by_category': amenities_by_category,
        'description': description,
        'GOOGLEMAPS_API_KEY': os.environ.get('GOOGLEMAPS_API_KEY', ''),
        'things_to_know_by_category': things_to_know_by_category,
        'no_of_bedrooms': no_of_bedrooms,
        'no_of_bathrooms': no_of_bathrooms,
    }

    return render(request, 'marketview_cottage.html', content)
