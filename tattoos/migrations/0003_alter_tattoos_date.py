# Generated by Django 5.1.1 on 2024-10-14 04:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoos', '0002_tattoos_date_tattoos_description_alter_tattoos_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tattoos',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 10, 13, 23, 38, 56, 499457)),
        ),
    ]
