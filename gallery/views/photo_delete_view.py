from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from gallery.models.photo import Photo


class PhotoDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'gallery/photo_delete.html'
    model = Photo
    success_url = reverse_lazy('list_view')
    permission_required = 'photos.can_delete_photo'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user