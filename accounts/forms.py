from django import forms


class UserRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()


class userLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
