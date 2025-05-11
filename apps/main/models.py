from django.db import models
from colorfield.fields import ColorField
from apps.extra.models import ImageType
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', _('Active')
        INACTIVE = 'inactive', _('Inactive')

    order = models.IntegerField(_("Order"), default=0)
    name = models.CharField(_("Name"), max_length=255)
    logo = models.ImageField(_("Logo"), upload_to='brands/logos/')
    zoom = models.FloatField(_("Zoom Level"), default=1.0)
    status = models.CharField(
        _("Status"), 
        max_length=255, 
        choices=Status.choices,
        default=Status.ACTIVE
    )

    class Meta:
        ordering = ['order']
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    @property
    def first_4_cars(self):
        return self.car_set.filter(status=Brand.Status.ACTIVE)[:4]

    @property
    def zoom_type(self):
        if self.zoom < 1:
            return 'zoom-in'
        elif self.zoom > 1:
            return 'zoom-out'
        return ''

    def __str__(self):
        return self.name


class Car(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', _('Active')
        INACTIVE = 'inactive', _('Inactive')

    class SpeedUnit(models.TextChoices):
        MINUTES = 'minutes', _('Minutes')
        HOURS = 'hours', _('Hours')

    order = models.IntegerField(_("Order"), default=0)
    brand = models.ForeignKey(
        Brand, 
        on_delete=models.RESTRICT, 
        verbose_name=_("Brand")
    )
    name = models.CharField(_("Name"), max_length=255)
    manufacture_year = models.IntegerField(_("Manufacture Year"), default=2023)
    price = models.DecimalField(
        _("Price"), 
        max_digits=10, 
        decimal_places=2
    )
    equipments = models.ManyToManyField(
        "extra.Equipment", 
        blank=True, 
        verbose_name=_("Equipment Packages")
    )
    engine_type = models.ForeignKey(
        "extra.EngineType", 
        on_delete=models.RESTRICT, 
        verbose_name=_("Engine Type")
    )
    acceleration = models.FloatField(_("Acceleration 0-100 km/h"))
    power_reserve_from = models.IntegerField(_("Power Reserve From"))
    power_reserve_to = models.IntegerField(_("Power Reserve To"))
    length = models.FloatField(_("Length (mm)"))
    width = models.FloatField(_("Width (mm)"))
    height = models.FloatField(_("Height (mm)"))
    seating_capacity = models.IntegerField(_("Seating Capacity"))
    max_speed = models.IntegerField(_("Max Speed (km/h)"))
    drive_unit = models.ForeignKey(
        "extra.DriveUnit", 
        on_delete=models.RESTRICT, 
        verbose_name=_("Drive Unit")
    )
    battery_capacity = models.FloatField(_("Battery Capacity (kWh)"))
    charging_speed = models.FloatField(_("Charging Speed"))
    speed_unit = models.CharField(
        _("Speed Unit"), 
        max_length=255, 
        choices=SpeedUnit.choices
    )
    description_1 = models.TextField(_("Description 1"), max_length=500)
    description_2 = models.TextField(_("Description 2"), max_length=500)
    is_featured = models.BooleanField(_("Featured"), default=False)
    status = models.CharField(
        _("Status"), 
        max_length=255, 
        choices=Status.choices,
        default=Status.ACTIVE
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    @property
    def formatted_price(self):
        return f"${self.price:,.2f}"

    def _get_images_by_type(self, slug_name):
        try:
            image_type = ImageType.objects.get(slug_name=slug_name)
            return self.carimage_set.filter(
                status=CarImage.Status.ACTIVE,
                image_types=image_type
            )
        except ImageType.DoesNotExist:
            return CarImage.objects.none()

    @property
    def images(self):
        return self.carimage_set.filter(status=CarImage.Status.ACTIVE)

    @property
    def main_images(self):
        return self._get_images_by_type('main_image')

    @property
    def poster_images(self):
        return self._get_images_by_type('poster_image')

    @property
    def inner_images(self):
        return self._get_images_by_type('inner_image')

    @property
    def two_inner_images(self):
        return self.inner_images[:2]

    @property
    def sensor_images(self):
        return self._get_images_by_type('sensor_image')

    @property
    def skillet_images(self):
        return self._get_images_by_type('skillet_image')

    @property
    def first_image(self):
        return self.main_images.first()

    @property
    def poster_image(self):
        return self.poster_images.first()

    @property
    def inner_image(self):
        return self.inner_images.first()

    @property
    def sensor_image(self):
        return self.sensor_images.first()

    @property
    def skillet_image(self):
        return self.skillet_images.first()

    def __str__(self):
        return self.name


class CarColor(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', _('Active')
        INACTIVE = 'inactive', _('Inactive')

    car = models.ForeignKey(
        Car, 
        on_delete=models.RESTRICT, 
        verbose_name=_("Car")
    )
    order = models.IntegerField(_("Order"), default=0)
    primary_color = ColorField(_("Primary Color"))
    secondary_color = ColorField(_("Secondary Color"), blank=True, null=True)
    status = models.CharField(
        _("Status"), 
        max_length=255, 
        choices=Status.choices,
        default=Status.ACTIVE
    )

    class Meta:
        ordering = ['order']
        verbose_name = _("Car Color")
        verbose_name_plural = _("Car Colors")

    def __str__(self):
        return f"{self.order} | {self.car}"


class CarImage(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', _('Active')
        INACTIVE = 'inactive', _('Inactive')

    car = models.ForeignKey(
        Car, 
        on_delete=models.RESTRICT, 
        verbose_name=_("Car")
    )
    image_types = models.ManyToManyField(
        "extra.ImageType", 
        blank=True, 
        verbose_name=_("Image Types")
    )
    order = models.IntegerField(_("Order"), default=0)
    image = models.ImageField(
        _("Image"), 
        upload_to='cars/images/%Y/%m/%d/'
    )
    status = models.CharField(
        _("Status"), 
        max_length=255, 
        choices=Status.choices,
        default=Status.ACTIVE
    )

    class Meta:
        ordering = ['car', 'order']
        verbose_name = _("Car Image")
        verbose_name_plural = _("Car Images")

    @property
    def image_types_list(self):
        return ", ".join([it.name for it in self.image_types.all()])

    def __str__(self):
        return f"{self.order} | {self.car}"