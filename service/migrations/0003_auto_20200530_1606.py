# Generated by Django 3.0.6 on 2020-05-30 09:06

from django.db import migrations, models
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=service.models.path_file_name),
        ),
    ]
