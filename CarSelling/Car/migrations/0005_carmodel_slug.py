# Generated by Django 4.2.7 on 2023-12-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0004_remove_carmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
