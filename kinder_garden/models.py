from django.db import models

# Create your models here.

class Banner(models.Model):
    banner_image = models.ImageField(upload_to='images/', )


class SchoolClasses(models.Model):
    photo = models.ImageField(upload_to='images/')
    lesson_name = models.CharField(max_length=200)
    duration = models.IntegerField()
    children = models.IntegerField(null=True, blank=True)

class PhotoGallery(models.Model):
    photo = models.ImageField(upload_to='images/')