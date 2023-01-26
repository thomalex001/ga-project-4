from django.urls import path
from .views import TypeListView, TypeDetailView

urlpatterns = [
    path('', TypeListView.as_view()),
    path('<int:pk>/', TypeDetailView.as_view())
]
