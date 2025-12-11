# warga/views.py

from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView 
)

from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm 
from .serializers import PengaduanSerializer, WargaSerializer 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'semua_pengaduan'

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

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' 
    success_url = reverse_lazy('warga-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html' 
    success_url = reverse_lazy('pengaduan-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-nik') 
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat'] 
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi'] 


class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-tanggal_lapor') 
    serializer_class = PengaduanSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'deskripsi']
    ordering_fields = ['status', 'tanggal_lapor']