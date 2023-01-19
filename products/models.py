from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):  # the Album class is inheriting properties from models.Model
    # this creates the title column and says the data type is a Char(50)
    # type = models.ManyToManyField(
    #     'type.Type', related_name="products",  blank=True)
    # name = models.CharField(max_length=50)
    # size = models.ManyToManyField(
    #     'size.Size', related_name="albums",  blank=True)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=300)
    # owner = models.ForeignKey(
    #     'jwt_auth.User',
    #     related_name="product",
    #     on_delete=models.CASCADE
    # )


    def __str__(self):
        return f"{self.brand} - {self.color}"