# Generated by Django 4.1.6 on 2023-02-17 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_car_brand_zoom_car_image_car_color_car_brand_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car_image",
            options={
                "ordering": ["order"],
                "verbose_name": "Фотография машины",
                "verbose_name_plural": "Фотографии машин",
            },
        ),
    ]
