# Generated by Django 3.2.21 on 2023-10-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hill', '0015_auto_20231015_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cottageimages',
            name='room_category',
            field=models.CharField(blank=True, choices=[('Living Room', 'Living Room'), ('Kitchen', 'Kitchen'), ('Dining Room', 'Dining Room'), ('Bedroom1', 'Bedroom1'), ('Bedroom2', 'Bedroom2'), ('Bathroom', 'Bathroom'), ('WC', 'WC'), ('Garden', 'Garden'), ('Parking', 'Parking'), ('Exterior', 'Exterior'), ('House Sign', 'House Sign'), ('Scenic Views', 'Scenic Views')], max_length=50, null=True),
        ),
    ]
