from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):  
    type = models.ForeignKey(
        'type.Type', related_name="products",  blank=True, on_delete=models.CASCADE)
    dimensions = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name="products",
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.brand} - {self.color}"