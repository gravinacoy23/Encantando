# Generated by Django 4.1.6 on 2023-02-12 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_remove_employeesinfo_género_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesinfo',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 12, 20, 24, 23, 531811, tzinfo=datetime.timezone.utc)),
        ),
    ]
