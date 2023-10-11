from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'user',
            'cottage',
            'check_in_date',
            'check_out_date',
            'number_of_guests',
            'guest_name',
        ]

