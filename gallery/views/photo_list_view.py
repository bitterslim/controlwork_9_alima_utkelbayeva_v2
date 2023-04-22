from django.views.generic import ListView

from gallery.models.photo import Photo


class PhotoListView(ListView):
    template_name = 'gallery/list_view.html'
    model = Photo
    context_object_name = 'photos'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset().all()
        queryset = queryset.order_by('-created_at')
        return queryset