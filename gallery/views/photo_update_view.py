from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from gallery.forms import PhotoForm
from gallery.models.photo import Photo


class PhotoUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'gallery/photo_update.html'
    model = Photo
    form_class = PhotoForm
    context_object_name = 'photos'
    permission_required = 'gallery.photo.can_change_photo'
    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

