from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import StockData
from .serializers import StockSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = StockData.objects.all()
    serializer_class = StockSerializer