

from django import forms

class PostForm(forms.ModelForm):

    def clean(self):
        title = self.cleaned_data['title']
        if not title.istitle():
            raise forms.ValidationError({'title': "Not a proper titlecased string"})