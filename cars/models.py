from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    car_name = models.CharField(max_length=100)

    car_model = models.CharField(max_length=100)

    car_price = models.IntegerField()

    car_color = models.CharField(max_length=50)

    def __str__(self):
        return self.car_name