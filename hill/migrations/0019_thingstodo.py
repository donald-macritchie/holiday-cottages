# Generated by Django 3.2.21 on 2023-10-16 14:27

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hill', '0018_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThingsToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('walks', 'walks'), ('pubs', 'pubs'), ('attractions', 'attractions')], default='', max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255)),
                ('site_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
