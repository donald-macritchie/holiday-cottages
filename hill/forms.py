from django import forms
from django.conf import settings
from django.core.mail import send_mail
from .models import Cottage, Booking, ContactMessage




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


class BookingForm(forms.ModelForm):
    check_in_date = forms.DateField(
        # Allow 'DD-MM-YYYY' or 'YYYY-MM-DD' formats
        input_formats=['%d-%m-%Y', '%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={'type': 'date', 'placeholder': 'DD-MM-YYYY'})
    )
    check_out_date = forms.DateField(
        # Allow 'DD-MM-YYYY' or 'YYYY-MM-DD' formats
        input_formats=['%d-%m-%Y', '%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={'type': 'date', 'placeholder': 'DD-MM-YYYY'})
    )

    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date',
                  'number_of_guests', 'guest_name']
