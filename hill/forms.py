from django import forms
from django.conf import settings
from django.core.mail import send_mail
from .models import Cottage, Booking, ContactMessage
# from bootstrap_datepicker_plus import DatePickerInput




class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'inquiry', 'message']

    def get_info(self):

        cleaned_data = self.cleaned_data

        name = cleaned_data.get('name').strip()
        from_email = cleaned_data.get('email')
        subject = cleaned_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cleaned_data.get('message')

        return subject, msg

    def send(self):
        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )


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
        fields = ['check_in_date', 'check_out_date', 'number_of_guests', 'guest_name']
