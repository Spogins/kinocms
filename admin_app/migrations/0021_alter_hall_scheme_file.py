# Generated by Django 4.1.1 on 2022-12-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0020_hall_scheme_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='scheme_file',
            field=models.CharField(max_length=100, null=True),
        ),
    ]