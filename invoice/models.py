from django.db import models

# Create your models here.
class Profile(models.Model):

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-time']
