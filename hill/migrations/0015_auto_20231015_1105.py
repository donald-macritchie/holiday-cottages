# Generated by Django 3.2.21 on 2023-10-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hill', '0014_cottageimages_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='cottageimages',
            name='cottage_category',
            field=models.CharField(blank=True, choices=[('Homestead', 'Homestead'), ('Marketview', 'Marketview')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cottageimages',
            name='room_category',
            field=models.CharField(blank=True, choices=[('Living Room', 'Living Room'), ('Kitchen', 'Kitchen'), ('Dining Room', 'Dining Room'), ('Bedroom', 'Bedroom'), ('Bathroom', 'Bathroom'), ('WC', 'WC'), ('Garden', 'Garden'), ('Parking', 'Parking'), ('Exterior', 'Exterior'), ('House Sign', 'House Sign'), ('Scenic Views', 'Scenic Views')], max_length=50, null=True),
        ),
    ]
