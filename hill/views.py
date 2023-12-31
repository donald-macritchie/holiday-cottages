from django.shortcuts import render, get_object_or_404, redirect
from .models import Cottage, CottageImages, Amenities, ThingsToKnow, ThingsToDo, Booking, HostDetails
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
        'images': images,
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
        'images': images,
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
                    return redirect('booking_confirmation', booking_id=booking.id)
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


# Booking confirmation


@login_required
def booking_confirmation(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        messages.error(request, "Booking not found.")
        return redirect('index')

    return render(request, 'booking_confirmation.html', {'booking': booking})


# User Profile
@login_required
def user_profile(request):
    user = request.user
    user_bookings = Booking.objects.filter(user=user).order_by('check_in_date')
    context = {
        'user': user,
        'user_bookings': user_bookings,
    }
    return render(request, 'profile.html', context)


# Edit booking

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        # Create a copy of the request.POST
        request_POST = request.POST.copy()

        # Parse the date strings into datetime objects
        request_POST['check_in_date'] = datetime.strptime(
            request.POST['check_in_date'], '%Y-%m-%d')
        request_POST['check_out_date'] = datetime.strptime(
            request.POST['check_out_date'], '%Y-%m-%d')

        # Create a BookingForm instance without an existing instance
        form = BookingForm(request_POST, instance=booking)

        # Check if any errors exist in the form
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']

            today = date.today()
            max_booking_date = today + \
                timedelta(days=180)  # 6 months in advance

            if today <= check_in_date < check_out_date <= max_booking_date:
                cottage_id = booking.cottage.id
                cottage = Cottage.objects.get(id=cottage_id)

                # Check if the selected dates are available for this cottage
                if not Booking.objects.filter(cottage=cottage, check_in_date__lt=check_out_date, check_out_date__gt=check_in_date).exists():
                    booking = form.save(commit=False)
                    booking.user = request.user
                    # booking.cottage = cottage
                    booking.save()
                    messages.success(request, "Booking Saved!")
                    return redirect('user_profile')
                else:
                    messages.error(
                        request, "The selected dates are not available for this cottage.")
            else:
                messages.error(request, "Invalid booking dates.")
    else:
        form = BookingForm(instance=booking)
        cottage_id = booking.cottage.id
        cottage = Cottage.objects.get(id=cottage_id)

    return render(request, 'edit_booking.html', {'form': form, 'booking': booking})


# Delete Booking
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        # Delete the booking
        booking.delete()
        return redirect('user_profile')

    return render(request, 'delete_booking.html', {'booking': booking})


# Contact


def host_details(request):
    host_details = HostDetails.objects.first()

    return render(request, 'contact.html', {'host_details': host_details})


def things_to_do(request):
    walks = ThingsToDo.objects.filter(category='walks')
    pubs = ThingsToDo.objects.filter(category='pubs')
    attractions = ThingsToDo.objects.filter(category='attractions')
    return render(
        request,
        'things_to_do.html',
        {'walks': walks, 'pubs': pubs, 'attractions': attractions}
    )
