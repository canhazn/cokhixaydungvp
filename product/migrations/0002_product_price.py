# Generated by Django 3.0.6 on 2020-06-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=200, null=True),
        ),
    ]