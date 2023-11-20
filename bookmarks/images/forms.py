import requests
from django import forms
from django.core.files.base import ContentFile
from django.forms import HiddenInput
from django.utils.text import slugify

from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'url']
        widgets = {'url': forms.HiddenInput()}

    def cleaned_url(self):
        url = self.cleaned_data['url']
        valid_extension = ['jpeg', 'png', 'jpg']
        extension = url.rsipilit('.', 1)[1].lower()
        if extension not in valid_extension:
            raise forms.ValidationError('given url does not match valid given extension')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsipilit('.', 1)[1].lower()
        image_name = f"{name}.{extension}"
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)
        if commit:
            image.save()
        return image
