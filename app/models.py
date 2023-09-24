from django.db import models
from django.core.exceptions import ValidationError
import re

# Custom phone number validator


def validate_phone_number_format(value):
    if not value or not re.match(r'^\d{3}-\d{3}-\d{4}$', value):
        raise ValidationError(
            'Phone number must be in the format xxx-xxx-xxxx')

# Create your models here.


class House(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='houses', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    total_number_of_beds = models.IntegerField()
    number_of_beds_open = models.IntegerField()
    parking_capacity = models.IntegerField()
    house_manager = models.CharField(max_length=100)
    house_manager_phone_number = models.CharField(
        max_length=12, validators=[validate_phone_number_format])
    cost_of_rent = models.IntegerField()
    rent_interval = models.CharField(max_length=100)
    sober_living_house = models.BooleanField()


class Resident(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='residents', on_delete=models.CASCADE)
    house = models.ForeignKey(
        House, related_name='residents', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, validators=[
                                    validate_phone_number_format])
    is_employed = models.BooleanField()
    felony_record = models.BooleanField()
    taking_psych_meds = models.BooleanField()
