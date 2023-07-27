from  django import forms
from movieapp.models import Movies


class moviesform(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','des','year','img']
