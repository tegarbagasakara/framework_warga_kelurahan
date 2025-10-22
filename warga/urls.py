# warga/urls.py

from django.urls import path
from .views import WargaListView, WargaDetailView, PengaduanListView 

urlpatterns = [
    # 1. Daftar Semua Pengaduan (http://127.0.0.1:8000/pengaduan/) - HARUS DI ATAS PK
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'), 
    
    # 2. Daftar Warga (http://127.0.0.1:8000/)
    path('', WargaListView.as_view(), name='warga-list'), 
    
    # 3. Detail Warga (http://127.0.0.1:8000/1/)
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'), 
]