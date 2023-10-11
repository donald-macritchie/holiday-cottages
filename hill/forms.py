from django import forms
from .models import Booking, ContactMessage


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


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

