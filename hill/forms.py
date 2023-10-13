from django import forms
from django.conf import settings
from django.core.mail import send_mail
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
        fields = ['name', 'email', 'inquiry', 'message']

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
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