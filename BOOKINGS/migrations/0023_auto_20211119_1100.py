# Generated by Django 3.2.9 on 2021-11-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKINGS', '0022_auto_20211118_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manualbooking',
            name='BookingNumber',
        ),
        migrations.AddField(
            model_name='manualbooking',
            name='TrackingID',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
