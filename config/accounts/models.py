from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Direction(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=150)
    family = models.CharField(max_length=150)
    birthday = models.DateField(auto_now_add=True)
    direction = models.ForeignKey(
        Direction, on_delete=models.PROTECT, related_name='directions'),
    phone_number = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    password = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to='users', default='image/default_person_image.jpg')
    link_facebook = models.TextField(blank=True, null=True)
    link_instagram = models.TextField(blank=True, null=True)
    link_telegram = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
