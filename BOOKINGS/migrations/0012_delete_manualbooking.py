# Generated by Django 3.2.9 on 2021-11-10 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKINGS', '0011_remove_manualbooking_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='manualbooking',
        ),
    ]
