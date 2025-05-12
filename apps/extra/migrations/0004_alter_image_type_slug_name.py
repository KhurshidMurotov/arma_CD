
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0003_alter_image_type_slug_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_type',  
            name='slug_name',
            field=models.CharField(
                choices=[
                    ('main_image', 'main_image'),
                    ('poster_image', 'poster_image'),
                    ('inner_image', 'inner_image'),
                    ('sensor_image', 'sensor_image'),
                    ('skillet_image', 'skillet_image')
                ],
                max_length=255,
                unique=True,
                verbose_name='Unique Name'  

            ),
        ),
    ]