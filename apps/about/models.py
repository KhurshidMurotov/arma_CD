from django.db import models


class About(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_DEACTIVE = 'deactive'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_DEACTIVE, 'Deactive'),
    )

    name = models.CharField(max_length=255)

    logo = models.ImageField(upload_to='img/about/')

    address = models.CharField(max_length=255)
    working_time = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    last_video = models.FileField(

        upload_to='video/last_video/',
        null=True,
        blank=True
        )
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)


    class Meta:
        ordering = ['id']
        verbose_name = "About Company"
        verbose_name_plural = "About Companies"

    def __str__(self):
        return self.name


class Review(models.Model):

    name = models.CharField("Name", max_length=255)
    phone_number = models.CharField("Phone number", max_length=20)
    car = models.ForeignKey(
        "main.Car",
        on_delete=models.RESTRICT,
        verbose_name="Car",
        related_name='reviews'
    )
    time = models.DateTimeField("Time",auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self) -> str:

        return f"{self.name} - {self.car}"