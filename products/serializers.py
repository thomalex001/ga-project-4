from rest_framework import serializers
from .models import Product
from type.serializers.common import TypeSerializer
from jwt_auth.serializers.common import UserSerializer



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 


class PopulatedProductSerializer(ProductSerializer):
  type = TypeSerializer()
  owner = UserSerializer()