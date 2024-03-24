from django import forms
from django.core.validators import FileExtensionValidator


class BookForm(forms.Form):


    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['bin','wav'])] , label= 'binary file')
