"""
URL configuration for data_kelurahan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# data_kelurahan/urls.py

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    # 1. Path kosong ('') mengarahkan ke URL aplikasi 'warga'
    path('', include('warga.urls')), 
    
    # 2. Path 'admin/'
    path('admin/', admin.site.urls),
    
    # 3. Path 'warga/' (jika Anda tetap ingin memilikinya, meskipun ini duplikat)
    # path('warga/', include('warga.urls')), 
]