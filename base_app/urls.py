from django.urls import path
from .views import homepage, edit_stock_entry, StockDataView, another_visualization


urlpatterns = [
    path('', homepage, name='homepage'),
    path('edit/<int:entry_id>/', edit_stock_entry, name='edit_stock_entry'),
    path('api/stock-data/', StockDataView.as_view(), name='stock_data_api'),
    path('another_chart/', another_visualization, name='another_visualization'),
  
    ]