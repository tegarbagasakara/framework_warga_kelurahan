# warga/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView # Tambahkan CreateView
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm 

# --- Views Read (Sudah ada dari Tugas 1 & 2) ---

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'semua_pengaduan'

# --- Views Create (Baru dari Tugas 3) ---

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    # Redirect ke daftar warga setelah sukses
    success_url = reverse_lazy('warga-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    # Redirect ke daftar semua pengaduan setelah sukses
    success_url = reverse_lazy('pengaduan-list')