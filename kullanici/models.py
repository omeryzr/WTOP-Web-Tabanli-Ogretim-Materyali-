from django.db import models

# Create your models here.

class uye(models.Model):
        adi=models.CharField(max_length=50, blank=True)
        soyadi=models.CharField(max_length=50, blank=True)
        eposta=models.EmailField(max_length=50, blank=True)
        parola=models.CharField(max_length=50, blank=True)