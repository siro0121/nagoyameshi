# Generated by Django 5.1.5 on 2025-02-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoya', '0007_restaurant_created_at_restaurant_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='img',
            field=models.ImageField(blank=True, default='noImage.png', upload_to='media_local/'),
        ),
    ]
