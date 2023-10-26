from django import forms
from django.conf import settings
from django.core.mail import send_mail
from .models import Cottage, Booking



class BookingForm(forms.ModelForm):
    check_in_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    check_out_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date',
                  'number_of_guests', 'guest_name']
