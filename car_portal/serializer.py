from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Car

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class CarSerializer(serializers.ModelSerializer):

    year_of_manufacture = serializers.DateTimeField(format='%d:%m:%Y %H:%M', input_formats=['%d:%m:%Y %H:%M', ])
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ['owner', 'brand', 'brand_descr', 'car_model', 'model_descr', 'year_of_manufacture','complectation', 'complectation_descr']
        read_only_fields = ['owner']
