from django import forms


class UploadGpxForm(forms.Form):
    gpx = forms.FileField(required=True)
    description = forms.CharField(required=False, max_length=1024)
