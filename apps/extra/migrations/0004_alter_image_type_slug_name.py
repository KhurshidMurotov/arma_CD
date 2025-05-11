
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0003_alter_image_type_slug_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ImageType',  # Standardized naming
            name='slug_name',
            field=models.CharField(
                choices=[
                    ('main_image', 'Main Image'),
                    ('poster_image', 'Poster Image'),
                    ('inner_image', 'Inner Image'),  # New option
                    ('sensor_image', 'Sensor Image'),
                    ('skillet_image', 'Skillet Image')
                ],
                max_length=255,
                unique=True,
                verbose_name='Unique Name'  # Translated
            ),
        ),
    ]