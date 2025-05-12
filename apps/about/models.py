from django.db import models


class About(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_DEACTIVE = 'deactive'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_DEACTIVE, 'Deactive'),
    )

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='about/logo/')
    address = models.CharField(max_length=255)
    working_time = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    last_video = models.FileField(
        upload_to='about/videos/',
        null=True,
        blank=True
    )
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE
    )

    class Meta:
        ordering = ['id']
        verbose_name = "About Company"
        verbose_name_plural = "About Companies"

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    car = models.ForeignKey(
        "main.Car",
        on_delete=models.RESTRICT,
        related_name='reviews'
    )
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        indexes = [
            models.Index(fields=['-time']),
        ]

    def __str__(self):
        return f"{self.name} - {self.car}"