from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cottage, CottageImages, Amenities, ThingsToKnow, ThingsToDo, Booking
from .forms import BookingForm, ContactMessageForm
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
import os

#  Home Page
def index(request):
    return render(request, "index.html")

def cottage_view(request, cottage_name):
    cottage = get_object_or_404(Cottage, name=cottage_name)
    description = cottage.description

    # Import photos of the cottage
    images = CottageImages.objects.filter(cottage=cottage)
    cottage_image = CottageImages.objects.get(title='house_sign_1')

    # Amenities
    amenities = cottage.amenities.all()
    amenities_by_category = {}
    for category, _ in Amenities.CATEGORY_CHOICES:
        amenities_by_category[category] = amenities.filter(category=category)

    # Things to Know
    things_to_know_by_category = {}
    things_to_know = cottage.things_to_know.all()
    for category, _ in ThingsToKnow.CATEGORY_CHOICES:
        things_to_know_by_category[category] = things_to_know.filter(
            category=category)

    no_of_bedrooms = cottage.no_of_bedrooms
    no_of_bathrooms = cottage.no_of_bathrooms

    # BookingForm
    booking_form = BookingForm()

    content = {
        'cottage': cottage,
        'images': images,
        'amenities_by_category': amenities_by_category,
        'description': description,
        'GOOGLEMAPS_API_KEY': os.environ.get('GOOGLEMAPS_API_KEY', ''),
        'things_to_know_by_category': things_to_know_by_category,
        'no_of_bedrooms': no_of_bedrooms,
        'no_of_bathrooms': no_of_bathrooms,
        'booking_form': booking_form,
        'cottage_image_url': cottage_image.image.url,
    }

    return render(request, ['homestead_cottage.html', 'marketview_cottage.html'], content)


# Booking Section



# ContactMessage
class ContactMessage(FormView):
    template_name = 'contact.html'
    form_class = ContactMessageForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'success.html'



# Things to do

def things_to_do(request):
    walks = ThingsToDo.objects.filter(category='walks')
    pubs = ThingsToDo.objects.filter(category='pubs')
    attractions = ThingsToDo.objects.filter(category='attractions')
    return render(
        request,
        'things_to_do.html',
        {'walks': walks, 'pubs': pubs, 'attractions': attractions}
    )



