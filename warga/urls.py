# warga/urls.py

from django.urls import path
from .views import (
    WargaListView, 
    WargaDetailView, 
    PengaduanListView, 
    WargaCreateView,         # Import view baru
    PengaduanCreateView      # Import view baru
)

urlpatterns = [
    # Warga
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), # URL tambah Warga (Harus di atas path dinamis)
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    
    # Pengaduan
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
]