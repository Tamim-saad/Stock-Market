from django.urls import path
from .views import get_stock_data, index, update_stock_data  # Ensure these are correctly imported

urlpatterns = [
    path('', index, name='index'),  # Root URL message
    path('stock-data/', get_stock_data, name='stock-data'),  # Stock data fetch API
    path('update-stock/<int:id>/', update_stock_data, name='update-stock'),  # Stock data update API
]
