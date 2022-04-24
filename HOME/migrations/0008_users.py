# Generated by Django 3.2.9 on 2021-11-11 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HOME', '0007_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=50)),
                ('verified', models.BooleanField(default=False)),
                ('reg_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
