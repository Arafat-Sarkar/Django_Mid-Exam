# Generated by Django 4.2.7 on 2023-12-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0003_remove_brandmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
