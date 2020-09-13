from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class VehicleOwned(models.Model):
    make = models.CharField(max_length=50,blank=False, null=False, default='')
    model = models.CharField(max_length=50, blank=True, null=True,default='')
    VIN_number = models.CharField(max_length=50,blank=True, null=True, default='00000')
    date_of_purchase = models.DateField(blank=True, null=True, default=timezone.now())
    date_of_last_service = models.DateField(blank=True, null=True, default=timezone.now())
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('vehiclesown_detail', args=[str(self.id)])
