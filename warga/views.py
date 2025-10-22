# warga/views.py

from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView # Import UpdateView & DeleteView
)
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm 

# --- Views Read (CRUD: Read) ---

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'semua_pengaduan'

# --- Views Create (CRUD: Create) ---

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

# --- Views Update (CRUD: Update) ---

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' # Menggunakan template form yang sama
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html' # Menggunakan template form yang sama
    success_url = reverse_lazy('pengaduan-list')


# --- Views Delete (CRUD: Delete) ---

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')