from django.db import models


# Create your models here.


class Image_upload(models.Model):
    Name = models.CharField(max_length=50)
    Image = models.FileField()


class test(models.Model):
    name = models.CharField(max_length=50)


class image_groups:
    macro_name: str
    sky_name: str
    light_name: str
    thunder_name: str
