from django.urls import path
from .views import WargaListView, WargaDetailView # Import DetailView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    # Tambahkan path detail: menangkap ID warga
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'), 
]