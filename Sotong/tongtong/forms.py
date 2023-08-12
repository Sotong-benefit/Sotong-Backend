from django import forms
from .models import UploadedBenefit

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedBenefit
        fields = ('file','tag')