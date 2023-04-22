from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     favorites = models.ManyToManyField(
#         to='gallery.Photo',
#         through='gallery.Favorite',
#     )