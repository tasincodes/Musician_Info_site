from typing import Any
from django import forms
from django.core import validators
from first_app.models import *

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"
        # exclude = ['First_name']
        # fields = ('First_name') for including




## this is forms.py sec -1
# class user_form(forms.Form):

    # user_name = forms.CharField(label='User Name',widget=forms.TextInput(
    #     attrs ={'placeholder': "enter your name",'style':'width:300px'}))
    # user_dob = forms.DateField(label="date of birth",widget= forms.TextInput(
    #     attrs = {'type':'date'}))
    # user_email = forms.EmailField(label="email",widget=forms.TextInput(
    #     attrs ={'placeholder': "enter your email"}))

    # user_name = forms.CharField(validators=[validators.MaxLengthValidator(15)])
    
    # user_email = forms.EmailField()
    # user_vmail = forms.EmailField()
     
    # def clean(self) -> dict[str, Any]:
    #     all_clean_data = super().clean()
    #     user_email = all_clean_data['user_email']
    #     user_vmail = all_clean_data['user_vmail']

    #     if user_email != user_vmail:
    #         raise forms.ValidationError("feilds dont match")