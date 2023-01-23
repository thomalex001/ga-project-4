from .common import TypeSerializer
from products.serializers import ProductSerializer


class PopulatedTypeSerializer(TypeSerializer):

    products = ProductSerializer(many=True)
