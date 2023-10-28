from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime


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
    COTTAGE_CATEGORIES = [
        ('Homestead', 'Homestead'),
        ('Marketview', 'Marketview'),
    ]

    ROOM_CATEGORIES = [
        ('Living Room', 'Living Room'),
        ('Kitchen', 'Kitchen'),
        ('Dining Room', 'Dining Room'),
        ('Bedroom1', 'Bedroom1'),
        ('Bedroom2', 'Bedroom2'),
        ('Bathroom', 'Bathroom'),
        ('WC', 'WC'),
        ('Garden', 'Garden'),
        ('Parking', 'Parking'),
        ('Exterior', 'Exterior'),
        ('House Sign', 'House Sign'),
        ('Scenic Views', 'Scenic Views'),
    ]

    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE,
                                related_name='images')
    title = models.CharField(max_length=100, default='')
    image = CloudinaryField('image')
    cottage_category = models.CharField(
        max_length=50, choices=COTTAGE_CATEGORIES, blank=True, null=True)
    room_category = models.CharField(
        max_length=50, choices=ROOM_CATEGORIES, blank=True, null=True)

    def __str__(self):
        return self.title


class Amenities(models.Model):
    CATEGORY_CHOICES = (
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
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default='')

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cottage = models.ForeignKey(
        Cottage, on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.IntegerField(default=0)
    guest_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Booking for {self.user.username} at {self.cottage} - Check-in: {self.check_in_date}, Check-out: {self.check_out_date}"


class HostDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telephone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ThingsToDo(models.Model):
    THINGS_TO_DO_CATEGORY = (
        ('walks', 'walks'),
        ('pubs', 'pubs'),
        ('attractions', 'attractions')
    )

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50, choices=THINGS_TO_DO_CATEGORY, default='')
    description = models.TextField()
    location = models.TextField()
    image = CloudinaryField()
    site_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
