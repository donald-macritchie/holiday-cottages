import unittest
from .models import Cottage


class TestCottage(unittest.TestCase):

    def test_create_cottage(self):
        cottage = Cottage(
            name='Test Cottage',
            slug='test-cottage',
            description='A test cottage for unittests.',
            location='Test Location',
            price_per_night=100.00,
            no_of_bedrooms=2,
            no_of_bathrooms=1,
        )
        
        self.assertEqual(cottage.name, 'Test Cottage')

    def test_cottage_string_representation(self):

        cottage = Cottage(name='Test Cottage')
        self.assertEqual(str(cottage), 'Test Cottage')



if __name__ == '__main__':
    unittest.main()
