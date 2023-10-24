import unittest
from .views import homestead_cottage
from django.urls import reverse
from django.test import Client


class TestHomesteadCottageView(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    # Tests if the view returns a 200 status

    def test_homestead_cottage_view(self):
        response = self.client.get(reverse('homestead_cottage'))

        self.assertEqual(response.status_code, 200)

    # Test if the context data is passed to the template
    def test_homestead_cottage_context(self):
        response = self.client.get(reverse('homestead_cottage'))
        homestead_cottage = response.context['homestead_cottage']

        self.assertEqual(homestead_cottage.name, 'Homestead')
        


class TestBookingView(unittest.TestCase):
    def setUp(self):
        self.client = Client

    def test_booking_view_GET(self):
        response = self.client.get(reverse('booking'))
        
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()