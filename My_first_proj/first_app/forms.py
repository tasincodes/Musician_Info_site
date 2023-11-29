from django import forms


class user_form(forms.Form):
    user_name = forms.CharField(label='User Name',widget=forms.TextInput(attrs ={'placeholder': "enter your name",'style':'width:300px'}))
    user_dob = forms.DateField(label="date of birth",widget= forms.TextInput(attrs = {'type':'date'}))
    user_email = forms.EmailField(label="email",widget=forms.TextInput(attrs ={'placeholder': "enter your email"}))