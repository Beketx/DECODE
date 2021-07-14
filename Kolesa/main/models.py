# from django.db import models
#
# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
#
#
# class CityManager(models.Manager):
#
#     def order_by_name(self):
#         return self.filter().order_by('name')
#
# class City(models.Model):
#     name = models.CharField(max_length=150)
#
#     objects = CityManager()
#
#     def __str__(self):
#         return self.name
#
# class CarManager(models.Manager):
#
#     def order_by_name(self):
#         return self.filter().order_by('name')
#
# class Car(City):
#     description = models.TextField(blank=True)
#
#     objects = CarManager()
#
# class Category(City):
#     description = models.TextField(blank=True)
#
#

from django.db import models
from django.contrib.auth.models import User

class AbstractModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True


class CityManager(models.Manager):

    def order_by_name(self):
        return self.filter().order_by('name')

class City(AbstractModel):


    objects = CityManager()

    def __str__(self):
        return self.name

class CarManager(models.Manager):

    def order_by_name(self):
        return self.filter().order_by('name')

class Car(AbstractModel):


    objects = CarManager()
    def __str__(self):
        return self.name

class Category(AbstractModel):

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class EngineType(models.Model):
    name = models.CharField(max_length=120)
    is_electric = models.BooleanField(default=False)


class KP(models.Model):
    name = models.CharField(max_length=120)
    is_full_drive = models.BooleanField(default=False)
