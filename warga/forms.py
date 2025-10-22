# warga/forms.py

from django import forms
from .models import Warga, Pengaduan

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        # Fields yang akan ditampilkan di form
        fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']

# --- Form untuk Challenge ---
class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        # UBAH 'isi' menjadi 'deskripsi'
        fields = ['judul', 'deskripsi', 'pelapor', 'status']