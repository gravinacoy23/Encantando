# Generated by Django 4.1.5 on 2023-02-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='carnet_EPS',
            field=models.FileField(blank=True, null=True, upload_to='static/media/carnets/%Y/%m/%D/'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='fotocopia_cédula',
            field=models.FileField(blank=True, null=True, upload_to='static/media/cedulas/%Y/%m/%D/'),
        ),
    ]
