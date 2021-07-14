import os

from django.db import models

# Create your models here.
from rest_framework.exceptions import ValidationError

from auth_.models import User
from main.models import Car, City

class AbstractModelDiller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    publications = models.ForeignKey(to="Publications", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True
    # def __str__(self):
    #     return self.publications.title

class FavoritesManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)


class Favourites(AbstractModelDiller):

    objects = FavoritesManager

class Publications(models.Manager):
    def order_by_year(self):
        return self.filter().order_by('year')

MAX_FILE_SIZE = 1024000
ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png']

def developer_photos_size(value):
    if value.size > MAX_FILE_SIZE:
        raise ValidationError(f'max file size is: {MAX_FILE_SIZE}')

def developer_file_extension(value):
    split_ext = os.path.splitext(value.name)
    if len(split_ext) > 1:
        ext = split_ext[1]
        if not ext.lower() in ALLOWED_EXTENSIONS:
            raise ValidationError(f'not allowed file value extension, valid extensions: {ALLOWED_EXTENSIONS}')

class Publications(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="media",
                                  validators=[developer_photos_size,
                                              developer_file_extension],
                                   blank=True,
                                   null=True)

class ArchiveManager(models.Manager):
    def for_car(self, car):
        return self.filter(car=car)

class Archive(AbstractModelDiller):

    objects = ArchiveManager