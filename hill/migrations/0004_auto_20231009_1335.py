# Generated by Django 3.2.21 on 2023-10-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hill', '0003_cottage_things_to_know'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cottage',
            name='things_to_know',
        ),
        migrations.AddField(
            model_name='cottage',
            name='things_to_know',
            field=models.ManyToManyField(blank=True, to='hill.Cottage'),
        ),
    ]
