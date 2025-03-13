from django.db import models
from colorfield.fields import ColorField
from apps.extra.models import Image_type


class Brand(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    order = models.IntegerField("Очередь", default=0)
    name = models.CharField("Название", max_length=255)
    logo = models.ImageField("Логотип", upload_to='img/brands')
    zoom = models.FloatField("Маштаб", default=1)
    status = models.CharField("Статус", max_length=255, choices=status_types)

    class Meta:
        ordering = ['order',]
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    @property
    def first_4_cars(self):
        return Car.objects.filter(brand=self)[:4]

    @property
    def zoom_type(self):
        if self.zoom < 1:
            return 'zoom-in'
        elif self.zoom > 1:
            return 'zoom-out'
        else:
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

    order = models.IntegerField("Очередь", default=0)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT, verbose_name="Бренд")
    name = models.CharField("Название", max_length=255)
    manufacture_year = models.IntegerField("Год выпуска", default=20)
    price = models.FloatField("Цена")
    equipments = models.ManyToManyField("extra.Equipment", blank=True, verbose_name="Комплектация")
    engine_type = models.ForeignKey("extra.Engine_type", on_delete=models.RESTRICT, verbose_name="Тип двигателя")
    acceleration = models.FloatField("Разгон до 100 км/ч")
    power_reserver_from = models.IntegerField("Запас хода от")
    power_reserver_to = models.IntegerField("Запас хода до")
    length = models.FloatField("Длина")
    width = models.FloatField("Ширина")
    height = models.FloatField("Высота")
    num_of_places = models.IntegerField("Кол-во мест")
    max_speed = models.IntegerField("Макс. скорость")
    drive_unit = models.ForeignKey("extra.Drive_unit", on_delete=models.RESTRICT, verbose_name="Привод")
    battery_capacity = models.FloatField("Емкость аккумулятора")
    charging_speed = models.FloatField("Скорость зарядки")
    speed_in = models.CharField("", max_length=255, choices=speed_in_types)
    desc_1 = models.TextField("Описание 1", max_length=150)
    desc_2 = models.TextField("Описание 2", max_length=150)
    is_featured = models.BooleanField("В избранном", default=False)
    status = models.CharField("Статус", max_length=255, choices=status_types)
    date = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        ordering = ['order',]
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

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

    car = models.ForeignKey(Car, on_delete=models.RESTRICT, verbose_name="Машина")
    order = models.IntegerField("Очередь", default=0)
    color_1 = ColorField("Цвет 1", max_length=255)
    color_2 = ColorField("Цвет 2", max_length=255)
    status = models.CharField("Статус", max_length=255, choices=status_types)

    class Meta:
        ordering = ['order',]
        verbose_name = "Цвет машины"
        verbose_name_plural = "Цвета машин"

    def __str__(self) -> str:
        return f"{self.order} | {self.car}"


class Car_image(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    car = models.ForeignKey(Car, on_delete=models.RESTRICT, verbose_name="Машина")
    image_types = models.ManyToManyField("extra.Image_type", blank=True, verbose_name="Типы фотографии")
    order = models.IntegerField("Очередь", default=0)
    image = models.ImageField("Фотография", upload_to='img/cars')
    status = models.CharField("Статус", max_length=255, choices=status_types)

    class Meta:
        ordering = ['car', 'order']
        verbose_name = "Фотография машины"
        verbose_name_plural = "Фотографии машин"

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

