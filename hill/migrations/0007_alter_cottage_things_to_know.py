# Generated by Django 3.2.21 on 2023-10-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hill', '0006_auto_20231009_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cottage',
            name='things_to_know',
            field=models.ManyToManyField(blank=True, to='hill.ThingsToKnow'),
        ),
    ]
