from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Cottage(models.Model):
    id = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=300)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.ManyToManyField('Amenities', blank=True)
    no_of_bedrooms = models.IntegerField(default=0)
    no_of_bathrooms = models.IntegerField(default=0)
    things_to_know = models.ManyToManyField('ThingsToKnow', blank=True)

    def __str__(self):
        return self.name


class CottageImages(models.Model):
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE,
                                related_name='images')
    image = CloudinaryField('image')

    def __str__(self):
        return self.image


class Amenities(models.Model):
    CATEGORY_CHOICES = (
        ('Scenic Views', 'Scenic Views'),
        ('Bathroom', 'Bathroom'),
        ('Bedroom and Laundry', 'Bedroom and Laundry'),
        ('Entertainment', 'Entertainment'),
        ('Family', 'Family'),
        ('Heating and Cooling', 'Heating and Cooling'),
        ('Home Saftey', 'Home Saftey'),
        ('Internet', 'Internet'),
        ('Kitchen and Dining', 'Kitchen and Dining'),
        ('Property Features', 'Property Features'),
        ('Parking', 'Parking'),
        ('Services', 'Services'),
        ('Not Included', 'Not Included'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default='')

    def __str__(self):
        return self.name


class ThingsToKnow(models.Model):
    CATEGORY_CHOICES = (
        ('Checking in and out', 'Checking in and out'),
        ('During your stay', 'During your stay'),
        ('Additional Rules', 'Additional Rules'),
        ('Before you leave', 'Before you leave'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='')


    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.IntegerField(default=0)
    guest_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cottage.name} - {self.check_in_date} to {self.check_out_date}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"