# Generated by Django 4.2.7 on 2023-12-26 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0002_brandmodel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandmodel',
            name='slug',
        ),
    ]
