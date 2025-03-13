from django.db import models


class About(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    name = models.CharField("Название", max_length=255)
    logo = models.ImageField("Лого", upload_to='img/about')
    address = models.CharField("Адрес", max_length=255)
    working_time = models.CharField("Время работы", max_length=255)
    phone_number = models.CharField("Телефонный номер", max_length=255)
    last_video = models.FileField("Последнее видео", upload_to='video/last_video', null=True, blank=True)
    facebook = models.URLField("Фейсбук", max_length=1024)
    instagram = models.URLField("Инстаграм", max_length=1024)
    telegram = models.URLField("Телеграм", max_length=1024)

    class Meta:
        ordering = ['id',]
        verbose_name = "О компании"
        verbose_name_plural = "О компании"

    def __str__(self) -> str:
        return self.name


class Review(models.Model):

    name = models.CharField("Имя", max_length=255)
    phone_number = models.CharField("Телефонный номер", max_length=255)
    car = models.ForeignKey("main.Car", on_delete=models.RESTRICT, verbose_name="Машина")
    time = models.TimeField("Время")

    class Meta:
        ordering = ['id',]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self) -> str:
        return self.name

