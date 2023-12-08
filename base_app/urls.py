from django.urls import path
from .views import homepage, edit_stock_entry


urlpatterns = [
    path('', homepage, name='homepage'),
    path('edit/<int:entry_id>/', edit_stock_entry, name='edit_stock_entry'),
  
    ]