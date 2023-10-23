from django.shortcuts import render, get_object_or_404, redirect
from .models import Cottage, CottageImages, Amenities, ThingsToKnow, ThingsToDo, Booking, HostDetails
from .forms import ContactMessageForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from datetime import datetime, timedelta, date
from django.contrib import messages
import os

#  Home Page
def index(request):
    return render(request, "index.html")


# Homestead Cottage
def homestead_cottage(request):
    homestead_cottage = get_object_or_404(Cottage, name='Homestead')
    description = homestead_cottage.description

    # import photos of homestead

    images = CottageImages.objects.filter(cottage=homestead_cottage)
    homestead_image = CottageImages.objects.get(title='house_sign_1')


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
        'images' : images,
        'amenities_by_category': amenities_by_category,
        'description': description,
        'GOOGLEMAPS_API_KEY': os.environ.get('GOOGLEMAPS_API_KEY', ''),
        'things_to_know_by_category': things_to_know_by_category,
        'no_of_bedrooms': no_of_bedrooms,
        'no_of_bathrooms': no_of_bathrooms,
        'booking_form': booking_form,
        'homestead_image_url': homestead_image.image.url,
        'cottage': homestead_cottage,
    }

    return render(request, 'homestead_cottage.html', content)


# Marketview Cottage
def marketview_cottage(request):
    marketview_cottage = get_object_or_404(Cottage, name='Marketview')
    description = marketview_cottage.description

    # import photos of marketview

    images = CottageImages.objects.filter(cottage=marketview_cottage)
    marketview_image = CottageImages.objects.get(title='house_sign_1')


    # Amenities
    amenities = marketview_cottage.amenities.all()
    amenities_by_category = {}

    for category, _ in Amenities.CATEGORY_CHOICES:
        amenities_by_category[category] = amenities.filter(category=category)

    # Things to Know
    things_to_know_by_category = {}
    things_to_know = marketview_cottage.things_to_know.all()

    for category, _ in ThingsToKnow.CATEGORY_CHOICES:
        things_to_know_by_category[category] = things_to_know.filter(
            category=category)

    no_of_bedrooms = marketview_cottage.no_of_bedrooms
    no_of_bathrooms = marketview_cottage.no_of_bathrooms

    # BookingForm
    booking_form = BookingForm()

    content = {
        'marketview_cottage': marketview_cottage,
        'images' : images,
        'amenities_by_category': amenities_by_category,
        'description': description,
        'GOOGLEMAPS_API_KEY': os.environ.get('GOOGLEMAPS_API_KEY', ''),
        'things_to_know_by_category': things_to_know_by_category,
        'no_of_bedrooms': no_of_bedrooms,
        'no_of_bathrooms': no_of_bathrooms,
        'booking_form': booking_form,
        'marketview_image_url': marketview_image.image.url,
        'cottage': marketview_cottage,
    }

    return render(request, 'marketview_cottage.html', content)



# Booking Section

@login_required
def booking(request):
    if request.method == 'POST':
        # Create a copy of the request.POST
        request_POST = request.POST.copy()

        # Parse the date strings into datetime objects
        request_POST['check_in_date'] = datetime.strptime(
            request.POST['check_in_date'], '%Y-%m-%d')
        request_POST['check_out_date'] = datetime.strptime(
            request.POST['check_out_date'], '%Y-%m-%d')

        # Create a BookingForm instance without an existing instance
        form = BookingForm(request_POST)

        # Check if any errors exist in the form
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']

            today = date.today()
            max_booking_date = today + \
                timedelta(days=180)  # 6 months in advance

            if today <= check_in_date < check_out_date <= max_booking_date:
                cottage_id = request.GET.get('cottage_id')
                cottage = Cottage.objects.get(id=cottage_id)

                # Check if the selected dates are available for this cottage
                if not Booking.objects.filter(cottage=cottage, check_in_date__lt=check_out_date, check_out_date__gt=check_in_date).exists():
                    booking = form.save(commit=False)
                    booking.user = request.user
                    booking.cottage = cottage
                    booking.save()
                    messages.success(request, "Booking Saved!")
                    return redirect('index')
                else:
                    messages.error(
                        request, "The selected dates are not available for this cottage.")
            else:
                messages.error(request, "Invalid booking dates.")
    else:
        form = BookingForm()
        cottage_id = request.GET.get('cottage_id')
        cottage = Cottage.objects.get(id=cottage_id)

    return render(request, 'booking.html', {'form': form, 'cottage': cottage})


# User Profile
@login_required
def user_profile(request):
    user = request.user
    user_bookings = Booking.objects.filter(user=user)
    context = {
        'user': user,
        'user_bookings': user_bookings,
    }
    return render(request, 'profile.html', context)




# Host Details


def host_details(request):
    host_details = HostDetails.objects.all()

    context = {
        'host_details': host_details,
    }
    return render(request, 'contact.html', context)

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



