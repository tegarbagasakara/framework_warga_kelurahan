# warga/admin.py
from django.contrib import admin
from .models import Warga, Pengaduan # Import Pengaduan

admin.site.register(Warga)
admin.site.register(Pengaduan) # Daftarkan model Pengaduan