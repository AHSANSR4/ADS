# Generated by Django 3.2.9 on 2021-11-11 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0005_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]