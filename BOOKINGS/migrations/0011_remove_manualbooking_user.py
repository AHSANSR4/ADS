# Generated by Django 3.2.9 on 2021-11-10 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKINGS', '0010_alter_manualbooking_bookingnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manualbooking',
            name='user',
        ),
    ]
