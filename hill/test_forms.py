import unittest
from .forms import BookingForm
from datetime import date


class TestBookingForm(unittest.TestCase):

    # Test if the form is valid when all fields have correct data
    def test_valid_form(self):
        data = {
            'check_in_date': '31/12/2023',
            'check_out_date': '02/01/2024',
            'number_of_guests': 2,
            'guest_name': 'John Doe',
        }
        form = BookingForm(data=data)
        self.assertTrue(form.is_valid())

    # Test if the form is invalid when fields have missing or incorrect data
    def test_invalid_form(self):
        data = {
            'check_in_date': '31/12/2023',
            'check_out_date': '02/01/2022',
            'number_of_guests': '',
            'guest_name': 'John Doe',
        }
        form = BookingForm(data=data)
        self.assertFalse(form.is_valid())

    # Test if the date widgets render as expected
    def test_widgets(self):
        form = BookingForm()
        self.assertIn('type="date"', str(form['check_in_date']))
        self.assertIn('type="date"', str(form['check_out_date']))

    # Test if the form is correctly saving to the data to the model
    def test_save_to_model(self):
        data = {
            'check_in_date': '31/12/2023',
            'check_out_date': '02/01/2024',
            'number_of_guests': 2,
            'guest_name': 'John Doe',
        }

        form = BookingForm(data=data)
        self.assertTrue(form.is_valid())
        booking = form.save(commit=False)
        self.assertEqual(booking.check_in_date, date(2023, 12, 31))
        self.assertEqual(booking.check_out_date, date(2024, 1, 2))
        self.assertEqual(booking.number_of_guests, 2)
        self.assertEqual(booking.guest_name, 'John Doe')

    if __name__ == '__main__':
        unittest.main()
