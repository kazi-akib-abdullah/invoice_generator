from django.db import models

# Create your models here.
class Profile(models.Model):

    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    product_details = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-time']
