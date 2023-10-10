from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Cottage(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=300)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.ManyToManyField('Amenities', blank=True)
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
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

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

