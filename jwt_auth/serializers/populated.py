from .common import UserSerializer
from products.serializers import ProductSerializer


class PopulatedUserSerializer(UserSerializer):

    users = ProductSerializer(many=True)
