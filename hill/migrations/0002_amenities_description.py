# Generated by Django 3.2.21 on 2023-10-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hill', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenities',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]