from django.db import models


class Engine_type(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    name = models.CharField("Название", max_length=255)
    slug_name = models.CharField("Уникальное название", max_length=255)
    image = models.ImageField("Фотография", upload_to='img/engine_type')

    class Meta:
        ordering = ['id',]
        verbose_name = "Тип двигателя"
        verbose_name_plural = "Типы двигателей"

    def __str__(self) -> str:
        return self.name


class Drive_unit(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    order = models.IntegerField("Очередь", default=0)
    name = models.CharField("Название", max_length=255)

    class Meta:
        ordering = ['order',]
        verbose_name = "Привод"
        verbose_name_plural = "Приводы"

    def __str__(self) -> str:
        return self.name


class Equipment(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    order = models.IntegerField("Очередь", default=0)
    name = models.CharField("Название", max_length=255)
    status = models.CharField("Статус", max_length=255, choices=status_types)

    class Meta:
        ordering = ['order',]
        verbose_name = "Комплектация"
        verbose_name_plural = "Комплектации"

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

    order = models.IntegerField("Очередь", default=0)
    name = models.CharField("Название", max_length=255)
    slug_name = models.CharField("Уникальное название", max_length=255, choices=slug_names, unique=True)

    class Meta:
        ordering = ['order',]
        verbose_name = "Тип фотографии"
        verbose_name_plural = "Типы фотографий"

    def __str__(self) -> str:
        return self.name

