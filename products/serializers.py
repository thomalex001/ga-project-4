from rest_framework import serializers
from .models import Product
# from types.serializers.common import GenreSerializer
# from sizes.serializers.populated import PopulatedSizesSerializer



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 


# class PopulatedProductSerializer(AlbumSerializer):
#     genres = GenreSerializer(many=True)
#     comments = PopulatedCommentSerializer(many=True)
#     artist = ArtistSerializer()
