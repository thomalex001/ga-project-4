from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/types/', include('type.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/auth/', include('jwt_auth.urls')),
]
