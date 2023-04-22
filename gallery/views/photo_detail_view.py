from django.views.generic import DetailView

from gallery.models.photo import Photo


class PhotoDetailView(DetailView):
    template_name = 'gallery/photo_detail.html'
    model = Photo
    context_object_name = 'photos'
