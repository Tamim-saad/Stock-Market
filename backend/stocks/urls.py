from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from .models import StockData
# from .serializers import StockSerializer

# class StockViewSet(viewsets.ModelViewSet):
#     queryset = StockData.objects.all()
#     serializer_class = StockSerializer
    
    
    # backend/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from stocks import views

router = routers.DefaultRouter()
router.register(r'stocks', views.StockViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
