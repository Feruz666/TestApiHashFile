from django import forms

class FilesForm(forms.Form):
    docfile = forms.FileField(
        label='select a file',
        help_text='max. 42 mb'
    )

