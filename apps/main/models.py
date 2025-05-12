from django.db import models
from colorfield.fields import ColorField
from apps.extra.models import Image_type


class Brand(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )


    order = models.IntegerField("Order", default=0)
    name = models.CharField("Name", max_length=255)
    logo = models.ImageField("Logo", upload_to='img/brands')
    zoom = models.FloatField("Zoom Level", default=1.0)
    status = models.CharField("Status", 
        max_length=255, 
        choices=status_types
    )

    class Meta:
        ordering = ['order',]
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    @property
    def first_4_cars(self):
        return Car.objects.filter(brand=self)[:4]

    @property
    def zoom_type(self):
        if self.zoom < 1:
            return 'zoom-in'
        elif self.zoom > 1:
            return 'zoom-out'
        return ''

    def __str__(self) -> str:
        return self.name


class Car(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    speed_in_types = (
        ('minutes', 'minutes'),
        ('hours', 'hours'),
    )

    order = models.IntegerField("Order", default=0)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT, verbose_name="Brand")
    name = models.CharField("Name", max_length=255)
    manufacture_year = models.IntegerField("Manufacture Year", default=20)
    price = models.FloatField("Price")
    equipments = models.ManyToManyField("extra.Equipment", blank=True, verbose_name="Complectation")
    engine_type = models.ForeignKey("extra.Engine_type", on_delete=models.RESTRICT, verbose_name="Engine Type")
    acceleration = models.FloatField("Acceleration 0-100 km/h")
    power_reserver_from = models.IntegerField("Power Reserve From")
    power_reserver_to = models.IntegerField("Power Reserve To")
    length = models.FloatField("Length")
    width = models.FloatField("Width")
    height = models.FloatField("Height")
    num_of_places = models.IntegerField("Passenger Capacity")
    max_speed = models.IntegerField("Max Speed")
    drive_unit = models.ForeignKey("extra.Drive_unit", on_delete=models.RESTRICT, verbose_name="Drive Unit")
    battery_capacity = models.FloatField("Battery Capacity")
    charging_speed = models.FloatField("Charging Speed")
    speed_in = models.CharField("", max_length=255, choices=speed_in_types)
    desc_1 = models.TextField("Description 1", max_length=150)
    desc_2 = models.TextField("Description 2", max_length=150)
    is_featured = models.BooleanField("Featured", default=False)
    status = models.CharField("Status", max_length=255, choices=status_types)
    date = models.DateTimeField("Date", auto_now_add=True)


    class Meta:
        ordering = ['order',]
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    @property
    def formatted_price(self):
        return '{:7,.1f}'.format(self.price)

    @property
    def images(self):
        images = Car_image.objects.filter(car=self).filter(status='active')
        return images
    
    @property
    def main_images(self):
        main_image_type = Image_type.objects.get(slug_name='main_image')
        return self.images.filter(image_types__in=[main_image_type,])
    
    @property
    def poster_images(self):
        poster_image_type = Image_type.objects.get(slug_name='poster_image')
        return self.images.filter(image_types__in=[poster_image_type,])

    @property
    def inner_images(self):
        inner_image_type = Image_type.objects.get(slug_name='inner_image')
        return self.images.filter(image_types__in=[inner_image_type,])

    @property
    def two_inner_images(self):
        return self.inner_images[:2]

    @property
    def sensor_images(self):
        sensor_image_type = Image_type.objects.get(slug_name='sensor_image')
        return self.images.filter(image_types__in=[sensor_image_type,])

    @property
    def skillet_images(self):
        skillet_image_type = Image_type.objects.get(slug_name='skillet_image')
        return self.images.filter(image_types__in=[skillet_image_type,])

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

    def __str__(self) -> str:
        return self.name


class Car_color(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    car = models.ForeignKey(Car, on_delete=models.RESTRICT, verbose_name="Car")
    order = models.IntegerField("Order", default=0)
    color_1 = ColorField("Color 1", max_length=255)
    color_2 = ColorField("Color 2", max_length=255)
    status = models.CharField("Status", max_length=255, choices=status_types)

    class Meta:
        ordering = ['order',]
        verbose_name = "Car Color"
        verbose_name_plural = "Car Colors"

    def __str__(self) -> str:
        return f"{self.order} | {self.car}"



class Car_image(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    car = models.ForeignKey(Car, on_delete=models.RESTRICT, verbose_name="Car")
    image_types = models.ManyToManyField("extra.Image_type", blank=True, verbose_name="Image Types")
    order = models.IntegerField("Order", default=0)
    image = models.ImageField("Image", upload_to='img/cars')
    status = models.CharField("Status", max_length=255, choices=status_types)

    class Meta:
        ordering = ['car', 'order']
        verbose_name = "Car Image"
        verbose_name_plural = "Car Images"

    @property
    def image_types_list(self):
        list_str = ''
        for i, item in enumerate(self.image_types.all()):
            list_str += f"{item.name}"
            if self.image_types.count() - i != 1:
                list_str += ", "
        return list_str

    def __str__(self) -> str:
        return f"{self.order} | {self.car}"

