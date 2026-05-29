from django import forms

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