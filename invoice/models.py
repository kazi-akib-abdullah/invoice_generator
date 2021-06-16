from django.db import models

# Create your models here.
class Profile(models.Model):

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name