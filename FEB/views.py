from django.shortcuts import render

# Create your views here.
def prodi2(request):
    judul = ["Sarjana Managemen", "Sarjana Akuntansi", "Sarjana Ilmu Ekonomi Pembangunan", "Sarjana Ekonomi Syariah", "Diploma Akuntansi", "Diploma Marketing", "Diploma Perpajakan", "Diploma Keuangan Perbankan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfeb.html', konteks)