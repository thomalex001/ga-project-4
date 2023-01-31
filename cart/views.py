from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .serializers.common import CartSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Cart

class CartListView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        request.data['owner'] = request.user.id
        add_to_cart = CartSerializer(data=request.data)
        try:
            add_to_cart.is_valid()
            add_to_cart.save()
            return Response(add_to_cart.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({
                "detail": str(e),
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response("Unprocessable Entity", status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class CartDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_cart(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise NotFound(detail="Can't find that cart!")

    def get(self, request, pk):
        cart = self.get_cart(pk=pk)
        if cart.owner != request.user:
            raise PermissionDenied()
        serialized_cart = CartSerializer(cart)
        return Response(serialized_cart.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        cart_to_edit = self.get_cart(pk=pk)
        # if cart_to_edit.owner != request.user:
        #     raise PermissionDenied()

        updated_cart = CartSerializer(cart_to_edit, data=request.data)
        try:
            updated_cart.is_valid()
            updated_cart.save()
            return Response(updated_cart.data, status=status.HTTP_202_ACCEPTED)

        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            return Response({"detail": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, pk):
        try:
            cart_to_delete = self.get_cart(pk=pk)
            if cart_to_delete.owner != request.user:
                raise PermissionDenied()

            cart_to_delete.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            raise NotFound(detail="Cart not found")
