# Generated by Django 3.2.23 on 2023-12-07 14:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_review_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='/placeholder.png', max_length=255, verbose_name='image'),
        ),
    ]
