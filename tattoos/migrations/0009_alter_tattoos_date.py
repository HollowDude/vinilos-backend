# Generated by Django 5.1.1 on 2024-10-27 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoos', '0008_alter_tattoos_date_alter_tattoos_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tattoos',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 10, 26, 23, 34, 33, 839457)),
        ),
    ]
