# warga/api_urls.py

from django.urls import path
from .views import WargaListAPIView, WargaDetailAPIView # Import kedua View API

urlpatterns = [
    # Endpoint Daftar Warga
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    
    # Endpoint Detail Warga
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
]