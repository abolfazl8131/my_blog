from django.db import models

# Create your models here.

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name = 'آدرس آی پی ')
    
