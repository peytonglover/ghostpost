from django import forms
from homepage.models import Post

class AddPostForm(forms.Form):
    content=forms.CharField(max_length=280)
    boast_roast = forms.ChoiceField(choices=((False, 'Roast'), (True, 'Boast')))
    # roast = forms.BooleanField()

    