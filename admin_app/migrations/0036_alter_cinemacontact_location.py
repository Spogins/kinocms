# Generated by Django 4.1.1 on 2023-01-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0035_alter_cinemacontact_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemacontact',
            name='location',
            field=models.URLField(max_length=300),
        ),
    ]