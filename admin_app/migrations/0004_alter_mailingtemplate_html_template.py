# Generated by Django 4.1.1 on 2022-11-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_alter_mailingtemplate_html_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailingtemplate',
            name='html_template',
            field=models.FileField(blank=True, null=True, upload_to='templates/'),
        ),
    ]