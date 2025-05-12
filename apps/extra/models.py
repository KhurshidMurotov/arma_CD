from django.db import models

class Engine_type(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    name = models.CharField("Name", max_length=255)
    slug_name = models.CharField("Slug Name", max_length=255, unique=True)
    image = models.ImageField("Image", upload_to='img/engine_type')

    class Meta:
        ordering = ['id']
        verbose_name = "Engine Type"
        verbose_name_plural = "Engine Types"

    def __str__(self) -> str:
        return self.name


class Drive_unit(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    order = models.IntegerField("Order", default=0)
    name = models.CharField("Name", max_length=255)

    class Meta:
        ordering = ['order']
        verbose_name = "Drive Unit"
        verbose_name_plural = "Drive Units"

    def __str__(self) -> str:
        return self.name


class Equipment(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )


    order = models.IntegerField("Order", default=0)
    name = models.CharField("Name", max_length=255)
    status = models.CharField("Status", max_length=255, choices=status_types)

    class Meta:
        ordering = ['order']
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment Packages"

    def __str__(self) -> str:
        return self.name


class Image_type(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    slug_names = (
        ('main_image', 'main_image'),
        ('poster_image', 'poster_image'),
        ('inner_image', 'inner_image'),
        ('sensor_image', 'sensor_image'),
        ('skillet_image', 'skillet_image'),
    )

    order = models.IntegerField("Order", default=0)
    name = models.CharField("Name", max_length=255)
    slug_name = models.CharField(
        "Slug Name", 
        max_length=255, 
        choices=slug_names, 
        unique=True
    )

    class Meta:
        ordering = ['order']
        verbose_name = "Image Type"
        verbose_name_plural = "Image Types"

    def __str__(self) -> str:
        return self.name