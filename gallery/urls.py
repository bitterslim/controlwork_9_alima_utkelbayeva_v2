from django.urls import path

from gallery.views.photo_create_view import CreatePhotoView
from gallery.views.photo_delete_view import PhotoDeleteView
from gallery.views.photo_detail_view import PhotoDetailView
from gallery.views.photo_list_view import PhotoListView
from gallery.views.photo_update_view import PhotoUpdateView

urlpatterns = [
    path("", PhotoListView.as_view(), name='list_view'),
    path("photo/add/", CreatePhotoView.as_view(), name='photo_create'),
    path("photo/<int:pk>/detail", PhotoDetailView.as_view(), name='photo_detail'),
    path("photo/<int:pk>/update", PhotoUpdateView.as_view(), name='photo_update'),
    path("photo/<int:pk>/delete/", PhotoDeleteView.as_view(), name= "photo_delete"),
    path("photo/<int:pk>/confirm_delete/", PhotoDeleteView.as_view(), name= "confirm_delete"),
]