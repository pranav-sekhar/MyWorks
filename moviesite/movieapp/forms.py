from django import forms
from .models import Movie
from django.contrib.auth.models import User

#for add/edit view
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie  #connects form to Movie model(user entered data stored in Movie Table)
        fields = ['title','poster','description','release_date','actors','rating','category','trailer','added_by'] #list of fields that should appear on form
    
#for profile edit view
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User #connects form with User model
        fields = ['username','email']  #fields that should appear on form