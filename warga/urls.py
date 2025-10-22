# warga/urls.py

from django.urls import path
from .views import (
    WargaListView, 
    WargaDetailView, 
    WargaCreateView, WargaUpdateView, WargaDeleteView, # CRUD Warga
    PengaduanListView, 
    PengaduanCreateView, PengaduanUpdateView, PengaduanDeleteView # CRUD Pengaduan
)

urlpatterns = [
    # Warga
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), 
    
    # Path Detail, Edit, Hapus untuk Warga (Menggunakan <int:pk>)
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),
    
    # Pengaduan
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),

    # Path Edit, Hapus untuk Pengaduan (Challenge)
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),
]