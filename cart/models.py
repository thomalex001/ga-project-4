from django.db import models


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(
        "products.Product",
        related_name="cart",  
    )
    owner = models.ForeignKey(
        "jwt_auth.User",
        related_name="cart",
        on_delete=models.CASCADE
    )