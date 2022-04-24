# Generated by Django 3.2.9 on 2021-11-10 17:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKINGS', '0009_manualbooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualbooking',
            name='BookingNumber',
            field=models.CharField(default=uuid.uuid4, max_length=50),
        ),
    ]