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


class DriveUnit(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
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
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
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


class ImageType(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
    )

    IMAGE_TYPES = (
        ('main_image', 'Main Image'),
        ('poster_image', 'Poster Image'),
        ('inner_image', 'Inner Image'),
        ('sensor_image', 'Sensor Image'),
        ('skillet_image', 'Skillet Image'),
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