# Generated by Django 3.2.21 on 2023-10-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hill', '0013_contactmessage_inquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='cottageimages',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
