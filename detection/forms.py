# detection/forms.py
from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='Enter URL')

class ImageForm(forms.Form):
    image = forms.ImageField(label='Upload Screenshot')
