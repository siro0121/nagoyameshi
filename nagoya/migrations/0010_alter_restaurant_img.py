# Generated by Django 5.1.5 on 2025-02-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoya', '0009_alter_restaurant_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='img',
            field=models.ImageField(blank=True, default='noImage.png', upload_to='media/'),
        ),
    ]
