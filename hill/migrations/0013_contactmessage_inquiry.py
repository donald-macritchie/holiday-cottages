# Generated by Django 3.2.21 on 2023-10-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hill', '0012_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='inquiry',
            field=models.CharField(default=0, max_length=200),
        ),
    ]