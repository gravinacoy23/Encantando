# Generated by Django 4.1.5 on 2023-02-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0003_alter_employees_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='rut',
            field=models.FileField(blank=True, null=True, upload_to='static/media/ruts/%Y/%m/%D/'),
        ),
    ]