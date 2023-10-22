from django.shortcuts import render, get_object_or_404, redirect
from .models import Cottage, CottageImages, Amenities, ThingsToKnow, ThingsToDo, Booking, HostDetails
from .forms import ContactMessageForm, BookingForm
from django.contrib.auth.decorators import login_required
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
    existing_booking = Booking.objects.filter(user=request.user).first()

    if request.method == 'POST':
        # make a copy of the request.POST, becuase the request.POST is immutable
        request_POST = request.POST.copy()

        # turn the date strings into datetime objects and reassing back to the copy of the request.POST
        request_POST['check_in_date'] = datetime.strptime(
            request.POST['check_in_date'], '%Y-%m-%d')
        request_POST['check_out_date'] = datetime.strptime(
            request.POST['check_out_date'], '%Y-%m-%d')
        
        # add the request_Post to the Booking Form
        form = BookingForm(request_POST, instance=existing_booking)

        # check if any errors exist in the form
        print("ERRORS: ", form.errors)
        
        if form.is_valid():
            booking = form.save(commit=False)
            booking.cottage = Cottage.objects.get(id=request.GET.get('cottage_id'))
            booking.user = request.user
            booking.save()

            # check_out_date = form.cleaned_data['check_out_date']
            # number_of_guests = form.cleaned_data['number_of_guests']
            # guest_name = form.cleaned_data['guest_name']

            # today = date.today()
            # max_booking_date = today + timedelta(days=180)

            # if today <= check_in_date <= max_booking_date and today <= check_out_date <= max_booking_date and check_in_date < check_out_date:
            #     cottage_id = request.GET.get('cottage_id')
            #     cottage = Cottage.objects.get(id=cottage_id)
            #     if not Booking.objects.filter(cottage=cottage, check_in_date__lt=check_out_date, check_out_date__gt=check_in_date).exists():
            #         booking = form.save(commit=False)
            #         booking.user = request.user
            #         booking.cottage = cottage
            #         booking.save()
            #         messages.success(request, "Booking Saved!")
            #         return redirect('index')
            #     else:
            #         messages.error(
            #             request, "The selected dates are not available for this cottage.")
            # else:
            #     messages.error(request, "Invalid booking dates.")
            return redirect('/')
    else:
        form = BookingForm(instance=existing_booking)
        cottage_id = request.GET.get('cottage_id')
        cottage = Cottage.objects.get(id=cottage_id)

    return render(request, 'booking.html', {'form': form, 'existing_booking': existing_booking, "cottage": cottage})




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



