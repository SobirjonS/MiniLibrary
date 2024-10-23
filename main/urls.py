from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.MainAPIView.as_view(), name='main'),
]