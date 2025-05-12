

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extra", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ImageType",
            name="slug_name",
            field=models.CharField(
                choices=[
                    ("main_image", "Main Image"),
                    ("poster_image", "Poster Image"),
                ],
                max_length=255,
                verbose_name="Slug Name",
                unique=True
            ),
        ),
    ]