# Generated by Django 4.1.6 on 2023-02-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extra", "0002_alter_image_type_slug_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image_type",
            name="slug_name",
            field=models.CharField(
                choices=[
                    ("main_image", "main_image"),
                    ("poster_image", "poster_image"),
                    ("sensor_image", "sensor_image"),
                    ("skillet_image", "skillet_image"),
                ],
                max_length=255,
                unique=True,
                verbose_name="Уникальное название",
            ),
        ),
    ]
