from django.contrib.auth import get_user_model
from django.db import models

# from accounts.models import User


class Photo(models.Model):
    author = models.ForeignKey(
            verbose_name='Автор',
            to=get_user_model(),
            related_name='photo_author',
            null=False,
            blank=False,
            on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name='Изображение',
        null=True,
        blank=True,
        upload_to='images')

    inscription = models.CharField(
        verbose_name='Подпись',
        null=False,
        blank=False,
        max_length=300
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

# class Favorite(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         related_name='favorite_user',
#         verbose_name='Избранноое',
#         null=False,
#         on_delete=models.CASCADE
#     )
#     photo = models.ForeignKey(
#         to=Photo,
#         related_name='favorites',
#         related_query_name='favorite',
#         verbose_name='Избранноое',
#         null=False,
#         on_delete=models.CASCADE
#     )
#
#     class Meta:
#         unique_together = ('user', 'photo')
