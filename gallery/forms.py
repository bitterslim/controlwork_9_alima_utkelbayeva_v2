from django import forms

from gallery.models.photo import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'inscription')
