from django.db import models

# Create your models here.
class credential(models.Model):
    email = models.CharField(max_length=200, blank=True, null=True)
    password=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.email
    
