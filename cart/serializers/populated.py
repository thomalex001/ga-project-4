from .common import CartSerializer
from jwt_auth.serializers.common import UserSerializer


class PopulatedCartSerializer(CartSerializer):
    owner = UserSerializer()
