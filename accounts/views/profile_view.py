from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from gallery.models.photo import Photo


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        account = self.get_object()
        photos = Photo.objects.filter(author=account)
        kwargs['photos'] = photos
        return super().get_context_data(**kwargs)