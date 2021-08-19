from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='car_portal', null=True)
    brand = models.CharField(max_length=200)
    brand_descr = models.TextField()
    car_model = models.CharField(max_length=200)
    model_descr = models.TextField()
    year_of_manufacture = models.DateTimeField()
    complectation = models.CharField(max_length=200)
    complectation_descr = models.TextField()



