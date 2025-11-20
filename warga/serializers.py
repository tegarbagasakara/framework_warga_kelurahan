# warga/serializers.py

from rest_framework import serializers
from .models import Warga, Pengaduan # Pastikan Pengaduan juga diimpor (jika ada)

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        # Ekspos field yang dibutuhkan. Gunakan '__all__' jika ingin semua.
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon'] 

# Jika Anda memiliki model Pengaduan dan ingin membuat API-nya
class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        fields = '__all__'