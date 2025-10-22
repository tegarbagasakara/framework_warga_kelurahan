from django.views.generic import ListView, DetailView
from .models import Warga, Pengaduan 

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'semua_pengaduan'