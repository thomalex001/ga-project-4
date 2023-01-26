from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.populated import PopulatedTypeSerializer
from .serializers.common import TypeSerializer
from .models import Type


class TypeListView(APIView):

    def get(self, _request):
        types = Type.objects.all()
        serialized_types = TypeSerializer(types, many=True)
        return Response(serialized_types.data, status=status.HTTP_200_OK)


class TypeDetailView(APIView):
    def get(self, _request, pk):
        type = Type.objects.get(pk=pk)
        serialized_type = PopulatedTypeSerializer(type)
        return Response(serialized_type.data, status=status.HTTP_200_OK)
