# Generated by Django 5.1.1 on 2024-10-25 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tattoos', '0005_alter_tattoos_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tattoos',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 10, 25, 8, 23, 50, 198142)),
        ),
    ]
