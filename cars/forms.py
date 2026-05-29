from django import forms
from django.contrib.auth.models import User

from .models import Car


class CarForm(forms.ModelForm):

    class Meta:

        model = Car

        fields = [
            'car_name',
            'car_model',
            'car_price',
            'car_color'
        ]


class SimpleSignupForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
