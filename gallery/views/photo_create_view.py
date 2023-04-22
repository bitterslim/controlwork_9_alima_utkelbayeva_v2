from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from gallery.forms import PhotoForm
from gallery.models.photo import Photo


class CreatePhotoView(LoginRequiredMixin, CreateView):
    template_name = 'gallery/photo_create.html'
    model = Photo
    form_class = PhotoForm

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        if form.is_valid():
            inscription = form.cleaned_data.get('inscription')
            image = form.cleaned_data.get('image')
            author = request.user
            if not Photo.objects.filter(inscription=inscription).exists():
                post = Photo.objects.create(inscription=inscription, image=image, author=author)
        else:
            form = {'text' : 'Smth went wrong, photo did not added'}
        return redirect('list_view')

    def get_success_url(self):
        return redirect('list_view')
